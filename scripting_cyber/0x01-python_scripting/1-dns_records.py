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
        except (
            dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers,
        ):
            # Skip record types that cannot be resolved
            continue
        except Exception:
            # Any unexpected error → continue safely
            continue

    return results
