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
        r'"(?P<method>
