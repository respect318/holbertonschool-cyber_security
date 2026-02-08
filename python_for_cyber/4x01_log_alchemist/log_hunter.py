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
