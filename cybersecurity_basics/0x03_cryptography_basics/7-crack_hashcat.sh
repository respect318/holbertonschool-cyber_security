#!/bin/bash
hashcat -m 0 -a 0 "$1" /usr/share/wordlists/rockyou.txt --quiet || true; hashcat -m 0 --show "$1" 2>/dev/null | cut -d: -f2 | grep -v '^$' > 7-password.txt
