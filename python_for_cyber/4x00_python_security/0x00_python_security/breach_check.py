# -----------------------------
# Task 7: The Policy Engine
# -----------------------------
def check_policy(password: str) -> str:
    """
    Check password strength based on policy.
    Returns 'WEAK' or 'COMPLIANT'.
    
    Policy:
    - WEAK if length < 8
    - WEAK if contains only letters
    - WEAK if in common passwords list
    - Otherwise, COMPLIANT
    """
    # Define a small common passwords list
    common_passwords = {"password", "123456", "qwerty", "123456789", "abc123"}

    # Check length
    if len(password) < 8:
        return "WEAK"

    # Check if password contains only letters
    if password.isalpha():
        return "WEAK"

    # Check if password is in common passwords list
    if password in common_passwords:
        return "WEAK"

    # If all checks passed, password is compliant
    return "COMPLIANT"

# -----------------------------
# Example test usage
# -----------------------------
if __name__ == "__main__":
    # Sample passwords to test the policy engine
    test_passwords = [
        "12345",          # WEAK: too short
        "password",       # WEAK: common password
        "abcdefgh",       # WEAK: only letters
        "abc12345",       # COMPLIANT
        "P@ssw0rd2026"    # COMPLIANT
    ]

    # Print results for each test password
    for pwd in test_passwords:
        print(f"{pwd}: {check_policy(pwd)}")
