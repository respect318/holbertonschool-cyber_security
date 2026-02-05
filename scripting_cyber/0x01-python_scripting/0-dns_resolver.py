#!/usr/bin/env python3
"""
0-dns_resolver.py
Resolves a domain name to its IPv4 address using the socket library.
"""

import socket


def resolve_domain_to_ipv4(domain_name):
    """
    Resolve a domain name to its IPv4 address.

    Args:
        domain_name (str): The domain name to resolve

    Returns:
        str: IPv4 address if resolved successfully
        None: If the domain cannot be resolved (socket.gaierror)
        str: Error message for any other exception
    """
    try:
        return socket.gethostbyname(domain_name)
    except socket.gaierror:
        return None
    except Exception as e:
        return str(e)
