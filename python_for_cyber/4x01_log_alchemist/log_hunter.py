#!/usr/bin/env python3


def read_stream(file_path: str):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        return


import re

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
