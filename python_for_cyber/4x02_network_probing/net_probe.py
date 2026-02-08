#!/usr/bin/env python3
import socket


def check_port(ip: str, port: int) -> bool:
    """Check if a TCP port is open on the given IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main():
    print("NetProbe v1.0 initialized...")
    # Test examples
    print(f"Port 80 is open: {check_port('google.com', 80)}")
    print(f"Port 81 is open: {check_port('google.com', 81)}")


if __name__ == "__main__":
    main()
