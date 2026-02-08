#!/usr/bin/env python3
import socket


def check_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main():
    print("NetProbe v1.0 initialized...")


if __name__ == "__main__":
    main()
