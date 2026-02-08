#!/usr/bin/env python3
import socket

def check_port(ip: str, port: int) -> bool:
    """Check if a TCP port is open on a given IP or hostname."""
    try:
        # context manager ilə socket açılır
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 saniyə timeout
            s.connect((ip, port))
            return True  # Əgər connect() uğurlu oldu
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False  # Əgər timeout və ya connection refused oldu
        

def main():
    print("NetProbe v1.0 initialized...")
    # test üçün nümunə
    print(f"Port 80 is open: {check_port('google.com', 80)}")
    print(f"Port 81 is open: {check_port('google.com', 81)}")


if __name__ == "__main__":
    main()
