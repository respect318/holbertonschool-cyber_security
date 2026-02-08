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
