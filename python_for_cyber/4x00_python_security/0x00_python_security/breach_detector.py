#!/usr/bin/env python3
import argparse
import sys
import re

# -----------------------------
# Task 3: Safe Reader
# -----------------------------
def read_file(filename: str) -> list:
    """
    Safely read a file line by line.
    Handles FileNotFoundError and PermissionError.
    Returns list of lines if successful.
    """
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"[ERROR] Permission denied: {filename}", file=sys.stderr)
        sys.exit(1)

# -----------------------------
# Task 4: Data Cleaner
# -----------------------------
def clean_data(lines: list) -> list:
    """
    Sanitize input lines:
    - Strip leading/trailing whitespace
    - Ignore empty lines
    - Ignore lines starting with #
    """
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        clean_lines.append(line)
    return clean_lines

# -----------------------------
# Task 5: Format Validator
# -----------------------------
def validate_line(line: str) -> bool:
    """
    Check if line follows the email:password format.
    Email must contain @ and .
    Returns True if valid, False otherwise.
    """
    # Basic pattern: something before ":" + ":" + something after
    pattern = r"^[^:]+:.+$"
    if not re.match(pattern, line):
        return False

    email_part = line.split(":", 1)[0]
    if "@" not in email_part or "." not in email_part:
        return False

    return True

# -----------------------------
# Task 1+2: CLI + main()
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="BreachCheck v1.0 - Analyze breach files professionally"
    )

    parser.add_argument("-f", "--file", type=str, required=True, help="Input file path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("-o", "--output", type=str, help="Output report file path")

    args = parser.parse_args()

    # Task 3: Safe file read
    lines = read_file(args.file)

    # Task 4: Clean data
    clean_lines = clean_data(lines)

    # Task 5: Validate format
    valid_lines = [line for line in clean_lines if validate_line(line)]

    # Verbose info
    if args.verbose:
        print(f"[VERBOSE] File loaded successfully: {args.file}")
        print(f"[VERBOSE] Total clean lines: {len(clean_lines)}")
        print(f"[VERBOSE] Total valid lines: {len(valid_lines)}")
        if args.output:
            print(f"[VERBOSE] Output file: {args.output}")

    print("BreachCheck v1.0 startup...")

# Entry point
if __name__ == "__main__":
    main()
