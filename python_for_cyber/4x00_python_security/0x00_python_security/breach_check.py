#!/usr/bin/env python3
import hashlib

# -----------------------------
# Task 8: The Secure Hash
# -----------------------------
def hash_password(password: str, salt: str) -> str:
    """
    Hash a password securely using SHA-256 with a salt.

    Steps:
    1. Encode the password to bytes
    2. Append the salt (also encoded)
    3. Hash using SHA-256
    4. Return the hexadecimal digest string
    """
    # Encode password and salt to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Append salt
    combined = password_bytes + salt_bytes

    # Create SHA-256 hash
    hashed = hashlib.sha256(combined)

    # Return hexadecimal string
    return hashed.hexdigest()

# -----------------------------
# Example test usage
# -----------------------------
if __name__ == "__main__":
    test_passwords = [
        ("password123", "mysalt"),
        ("abc12345", "salt2026"),
        ("P@ssw0rd2026", "secure!")
    ]

    # Hash each password and print the result
    for pwd, salt in test_passwords:
        print(f"Password: {pwd} | Salt: {salt} | SHA-256: {hash_password(pwd, salt)}")
