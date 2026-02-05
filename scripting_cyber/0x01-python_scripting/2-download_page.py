#!/usr/bin/env python3
"""
2-download_page.py
Download a web page and return formatted HTML using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def download_page(url):
    """
    Download and format a web page's HTML content.

    Args:
        url (str): URL of the web page

    Returns:
        str: Formatted HTML content or error message
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()
    except requests.exceptions.RequestException as e:
        return str(e)
