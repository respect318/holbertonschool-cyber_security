#!/usr/bin/env python3
import requests


def get_http_headers(url):
    """
    Retrieves HTTP response headers from a website.

    Args:
        url (str): Target URL

    Returns:
        dict: {'status_code': int, 'headers': dict} if successful
        None: if request fails
    """
    try:
        response = requests.get(url, timeout=10)

        return {
            "status_code": response.status_code,
            "headers": dict(response.headers)
        }

    except requests.exceptions.RequestException:
        return None
