#!/usr/bin/env python3
import socket
import requests
from bs4 import BeautifulSoup


def dns_recon(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
    except socket.gaierror:
        print("Could not resolve domain to IP")
        return

    print("\nMX Records:")
    try:
        # MX lookup not available without external libraries
        print("  MX lookup not supported in this environment")
    except Exception:
        print("  Could not retrieve MX records")


def web_recon(domain):
    try:
        response = requests.get(f"https://{domain}", timeout=10)
        print(f"\nStatus Code: {response.status_code}")

        print("\nImportant Headers:")
        for key in ["Server", "Content-Type"]:
            if key in response.headers:
                print(f"  {key}: {response.headers[key]}")

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        print(f"\nTotal Links Found: {len(links)}")

    except requests.exceptions.RequestException as e:
        print(f"Web request failed: {e}")


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
