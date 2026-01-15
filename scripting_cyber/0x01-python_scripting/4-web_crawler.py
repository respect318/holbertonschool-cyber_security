#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(start_url, max_depth=2):
    visited = set()

    try:
        start_domain = urlparse(start_url).netloc
    except Exception:
        return set()

    def crawl(url, depth):
        if depth > max_depth:
            return

        if url in visited:
            return

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return

        visited.add(url)
        print(f"Crawling: {url}")

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(url, link["href"])
            parsed_url = urlparse(absolute_url)

            if parsed_url.scheme not in ("http", "https"):
                continue

            if parsed_url.netloc != start_domain:
                continue

            crawl(absolute_url, depth + 1)

    crawl(start_url, 0)
    return visited
