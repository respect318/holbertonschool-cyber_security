#!/usr/bin/env python3
import argparse
import sys
from utils import clean_data, validate_line, hash_password

# -----------------------------
# Task 3: Safe Reader
# -----------------------------
def read_file(filename: str) -> list:
    """
    Safely read a file line by line.
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
# Task 10: Main function
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="BreachCheck v1.0 - Refactored Package Example"
    )
    parser.add_argument("-f", "--file", required=True, help="Input file path")
    args = parser.parse_args()

    # Read file
    lines = read_file(args.file)
    cleaned = clean_data(lines)

    # Show cleaned lines
    print("Cleaned lines:", cleaned)

    # Validate each line and hash only valid passwords
    for line in cleaned:
        if validate_line(line):
            email, password = line.split(":", 1)
            print(f"{line} is valid")
            print("SHA-256 hash:", hash_password(password, "mysalt"))
        else:
            print(f"{line} skipped: invalid format")

# Entry point
if __name__ == "__main__":
    main()

