#!/usr/bin/env python3
"""
LogHunter - Stream reader
"""

def read_stream(file_path: str):
    """
    Reads a file line by line using a generator.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        return
