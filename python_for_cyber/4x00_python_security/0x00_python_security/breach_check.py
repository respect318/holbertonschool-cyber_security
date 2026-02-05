#!/usr/bin/env python3
import argparse
import sys

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
# Task 1+2: CLI + main()
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="BreachCheck v1.0 - Analyze breach files professionally"
    )

    # Required input file
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Input file path"
    )

    # Optional verbose
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose mode"
    )

    # Optional output
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output report file path"
    )

    args = parser.parse_args()

    # Task 3: Safe file read
    lines = read_file(args.file)

    # Verbose info
    if args.verbose:
        print(f"[VERBOSE] File loaded successfully: {args.file}")
        print(f"[VERBOSE] Total lines: {len(lines)}")
        if args.output:
            print(f"[VERBOSE] Output file: {args.output}")

    print("BreachCheck v1.0 startup...")

# Entry point
if __name__ == "__main__":
    main()
