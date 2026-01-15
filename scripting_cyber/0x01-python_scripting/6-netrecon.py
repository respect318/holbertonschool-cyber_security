#!/usr/bin/env python3
"""
Basic Network Reconnaissance Tool
Combines DNS, Web, and Port reconnaissance
"""

import socket
import requests
from bs4 import BeautifulSoup
import dns.resolver


# ---------------- DNS RECON ----------------
def dns_recon(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
    except socket.gaierror:
        print("Could not resolve domain to IP")
        return

    try:
        print("\nMX Records:")
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"  {rdata.preference} {rdata.exchange}")
    except (dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers):
        print("  No MX records found")
    except Exception as e:
        print(f"  DNS error: {e}")


# ---------------- WEB RECON ----------------
def web_recon(domain):
    url = f"https://{domain}"

    try:
        response = requests.get(url, timeout=10)
        print(f"\nStatus Code: {response.status_code}")

        print("\nImportant Headers:")
        headers = dict(response.headers)
        for key in ["Server", "Content-Type"]:
            if key in headers:
                print(f"  {key}: {headers[key]}")

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        print(f"\nTotal Links Found: {len(links)}")

    except requests.exceptions.RequestException as e:
        print(f"Web request failed: {e}")


# ---------------- PORT SCAN ----------------
def port_scan(domain):
    ports = [80, 443]

    print(f"\nScanning common ports on {domain}...")
    print("Open ports:")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((domain, port))
            sock.close()

            if result == 0:
                print(f"  Port {port}: OPEN")

        except Exception:
            continue
