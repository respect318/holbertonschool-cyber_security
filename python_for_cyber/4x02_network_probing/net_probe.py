#!/usr/bin/env python3
import socket

def check_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def ping_sweep(subnet: str) -> list:
    """
    Scan a /24 subnet by checking port 80 on hosts .1 to .254
    Returns a list of live IPs
    """
    live_hosts = []

    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        if check_port(ip, 80):
            live_hosts.append(ip)

    return live_hosts


def main():
    print("NetProbe v1.0 initialized...")
    print(ping_sweep("192.168.1"))


if __name__ == "__main__":
    main()
