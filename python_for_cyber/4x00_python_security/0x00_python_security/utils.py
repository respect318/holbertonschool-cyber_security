#!/usr/bin/env python3
import hashlib

# -----------------------------
# Task 4: Data Cleaner
# -----------------------------
def clean_data(lines: list) -> list:
    """
    Clean input lines:
    - strip whitespace
    - ignore empty lines
    - ignore lines starting with #
    """
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        clean_lines.append(line)
    return clean_lines

# -----------------------------
# Task 5: Format Validator
# -----------------------------
def validate_line(line: str) -> bool:
    """
    Validate line format: must be email:password
    """
    if ":" not in line:
        return False
    email, _ = line.split(":", 1)
    if "@" not in email or "." not in email:
        return False
    return True

# -----------------------------
# Task 8: Secure Hash
# -----------------------------
def hash_password(password: str, salt: str) -> str:
    """
    Hash a password with SHA-256 and salt
    """
    combined = password.encode("utf-8") + salt.encode("utf-8")
    return hashlib.sha256(combined).hexdigest()

