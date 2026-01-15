#!/usr/bin/env python3
"""
Check if a specific TCP port is open on a host
"""
import socket


def check_port(host, port):
    """
    Check if a TCP port is open on a given host.

    Args:
        host (str): Target hostname or IP
        port (int): Target port number

    Returns:
        True if port is open, False otherwise
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return True
        return False

    except Exception:
        return False
