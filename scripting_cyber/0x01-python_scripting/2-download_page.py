#!/usr/bin/env python3
"""
Download and format a web page HTML content using requests and BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup


def download_page(url):
    """
    Download a web page and return its formatted HTML content.

    Args:
        url (str): URL of the web page

    Returns:
        str: Prettified HTML content if successful
        str: Error message if download fails
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        return soup.prettify()

    except requests.exceptions.RequestException as e:
        return str(e)
