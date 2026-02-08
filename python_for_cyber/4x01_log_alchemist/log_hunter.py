#!/usr/bin/env python3

import re


def read_stream(file_path: str):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        return


def parse_apache_line(line: str) -> dict:
    pattern = (
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'
        r'\[(?P<date>[^\]]+)\]\s+'
        r'"(?P<method>[A-Z]+)\s+(?P<path>[^ ]+)[^"]*"\s+'
        r'(?P<status>\d{3})\s+'
        r'(?P<size>\d+)'
    )
    match = re.search(pattern, line)
    if not match:
        return None
    return match.groupdict()


def parse_syslog_line(line: str) -> dict:
    pattern = (
        r'(?P<date>[A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+'
        r'(?P<host>\S+)\s+'
        r'(?P<process>[^:]+):\s+'
        r'(?P<message>.+)'
    )
    match = re.search(pattern, line)
    if not match:
        return None
    return match.groupdict()


class LogEntry:
    def __init__(self, ip, timestamp, service, message, raw_line):
        self.ip = ip
        self.timestamp = timestamp
        self.service = service
        self.message = message
        self.raw_line = raw_line


def normalize_entry(parsed_dict, type):
    if not parsed_dict:
        return None
    if type == "apache":
        return LogEntry(
            ip=parsed_dict.get("ip"),
            timestamp=parsed_dict.get("date"),
            service="http",
            message=parsed_dict.get("path"),
            raw_line=None
        )
    if type == "syslog":
        return LogEntry(
            ip=None,
            timestamp=parsed_dict.get("date"),
            service="ssh",
            message=parsed_dict.get("message"),
            raw_line=None
        )
    return None


def filter_logs(entries, service=None, status=None):
    filtered = []
    for entry in entries:
        if service and entry.service != service:
            continue
        filtered.append(entry)
    return filtered


GEOIP_DB = {
    '1.2.3.4': 'US',
    '5.6.7.8': 'RU'
}


def enrich_ip(log_entry):
    if not hasattr(log_entry, 'ip') or log_entry.ip is None:
        log_entry.country = 'UNKNOWN'
    else:
        log_entry.country = GEOIP_DB.get(log_entry.ip, 'UNKNOWN')
    return log_entry


def analyze_user_agent(log_entry):
    """
    Checks if a LogEntry message contains automated tool User-Agent strings.
    If it contains sqlmap, nikto, curl, or python, sets log_entry.is_bot = True.
    Otherwise, sets is_bot = False.
    """
    if not hasattr(log_entry, 'message') or log_entry.message is None:
        log_entry.is_bot = False
        return log_entry

    bot_keywords = ['sqlmap', 'nikto', 'curl', 'python']

    message_lower = log_entry.message.lower()
    log_entry.is_bot = any(keyword in message_lower for keyword in bot_keywords)

    return log_entry
