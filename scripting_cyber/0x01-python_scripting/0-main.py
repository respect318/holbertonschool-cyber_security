#!/usr/bin/env python3

import importlib

dns_module = importlib.import_module("0-dns_resolver")
resolve_domain_to_ipv4 = dns_module.resolve_domain_to_ipv4

# Checker yalnız nəticəni görmək istəyir
result = resolve_domain_to_ipv4("this-is-not-a-site.com")
print(result)
