#!/usr/bin/env python3
"""
NetProbe v1.0
Python network probing toolkit (Level 0)
"""

import socket


def get_banner(ip: str, port: int) -> str:
    """
    Grab the banner from a service running on a specific port.

    Args:
        ip (str): IP address or hostname
        port (int): TCP port number

    Returns:
        str: The banner string, or "Unknown" if not received
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, port))
            # Send generic probe for HTTP ports
            if port == 80:
                s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024)
            return banner.decode(errors="ignore").strip()
    except (socket.timeout, ConnectionRefusedError, OSError):
        return "Unknown"


def main():
    """Test get_banner function."""
    print("NetProbe v1.0 initialized...")
    print(f"Banner on scanme.nmap.org:22 -> {get_banner('scanme.nmap.org', 22)}")


if __name__ == "__main__":
    main()
