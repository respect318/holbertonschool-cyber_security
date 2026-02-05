#!/usr/bin/env python3
"""
Query and return multiple DNS record types for a given domain
using dnspython.
"""

import dns.resolver


def query_dns_records(domain_name):
    """
    Query DNS records for a domain.

    Args:
        domain_name (str): Domain to query

    Returns:
        dict: Dictionary of DNS answers by record type
    """
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain_name, record_type)
            results[record_type] = answers
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            # Skip record types that cannot be resolved
            # Optional: log the missing record
            # print(f"{record_type} record not found for {domain_name}")
            continue
        except Exception as e:
            # Any unexpected error → continue safely
            # Optional: log unexpected errors
            # print(f"Error querying {record_type} for {domain_name}: {e}")
            continue

    return results


# Test block
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    records = query_dns_records(domain)

    for r_type, answers in records.items():
        print(f"\n{r_type} Records:")
        if r_type == "MX":
            for ans in answers:
                print(f"  • {ans.preference} {ans.exchange}")
        elif r_type == "SOA":
            for ans in answers:
                print(f"  • Primary: {ans.mname}, Admin: {ans.rname}, Serial: {ans.serial}")
        elif r_type == "TXT":
            for ans in answers:
                for txt in ans.strings:
                    print(f'  • "{txt.decode().strip()}"')
        else:
            for ans in answers:
                print(f"  • {ans}")
