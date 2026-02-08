#!/usr/bin/env python3
"""
NetProbe v1.0
Python network probing toolkit (Level 0)
"""

import socket


def check_port(ip: str, port: int) -> bool:
    """Check if a TCP port is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def get_banner(ip: str, port: int) -> str:
    """Grab the service banner from an open port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((ip, port))
            if port == 80:
                sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024)
            return banner.decode(errors="ignore").strip()
    except (socket.timeout, ConnectionRefusedError, OSError):
        return "Unknown"


def scan_ports(ip: str, start_port: int, end_port: int) -> list:
    """
    Scan a range of ports on a target host.

    Args:
        ip (str): Target IP address
        start_port (int): Starting port number
        end_port (int): Ending port number

    Returns:
        list: List of dictionaries with open ports and services
    """
    results = []

    print(f"Scanning {ip} from {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        if check_port(ip, port):
            service = get_banner(ip, port)
            print(f"[+] Port {port} Open: {service}")
            results.append(
                {
                    "port": port,
                    "service": service
                }
            )

    return results


def main():
    """Main entry point."""
    scan_ports("192.168.1.1", 20, 80)


if __name__ == "__main__":
    main()
