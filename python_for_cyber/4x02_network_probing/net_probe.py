#!/usr/bin/env python3
"""
NetProbe v1.0
Python network probing toolkit (Level 0)
"""

import socket


def check_port(ip: str, port: int) -> bool:
  """
  Check if a TCP port is open on a given IP or hostname.

  Args:
      ip (str): IP address or hostname
      port (int): TCP port number

  Returns:
      bool: True if port is open, False otherwise
  """
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(1)
      s.connect((ip, port))
      return True
  except (socket.timeout, ConnectionRefusedError, OSError):
    return False


def ping_sweep(subnet: str) -> list:
  """
  Scan a /24 subnet by checking port 80 on hosts .1 to .254.

  Args:
      subnet (str): Subnet prefix (e.g., "192.168.1")

  Returns:
      list: List of live IP addresses
  """
  live_hosts = []

  for i in range(1, 255):
    ip = f"{subnet}.{i}"
    if check_port(ip, 80):
      live_hosts.append(ip)

  return live_hosts


def get_banner(ip: str, port: int) -> str:
  """
  Grab the banner from a service running on a specific port.

  Args:
      ip (str): IP address or hostname
      port (int): TCP port number

  Returns:
      str: The banner string, or "Unknown" if not received
  """
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(2)
      s.connect((ip, port))
      # Send generic probe for HTTP ports
      if port == 80:
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
      banner = s.recv(1024)
      return banner.decode(errors="ignore").strip()
  except (socket.timeout, ConnectionRefusedError, OSError):
    return "Unknown"


def main():
  """Main entry point for NetProbe."""
  print("NetProbe v1.0 initialized...")
  print(f"Port 80 is open: {check_port('google.com', 80)}")
  print(f"Port 81 is open: {check_port('google.com', 81)}")
  print(f"Live hosts in 192.168.1.0/24: {ping_sweep('192.168.1')}")
  print(f"Banner on scanme.nmap.org:22 -> {get_banner('scanme.nmap.org', 22)}")


if __name__ == "__main__":
  main()
