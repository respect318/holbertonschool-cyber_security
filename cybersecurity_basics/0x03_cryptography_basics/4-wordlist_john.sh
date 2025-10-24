#!/bin/bash
[[ -z "${1:-}" ]] && { echo "Usage: $0 <hash_file>"; exit 1; }; [[ -f /usr/share/wordlists/rockyou.txt ]] && WL=/usr/share/wordlists/rockyou.txt || WL=<(zcat /usr/share/wordlists/rockyou.txt.gz 2>/dev/null) || WL=wordlist.txt; john --wordlist="$WL" "$1" && john --show "$1" | awk -F: '/:/{print $2}' | sed '/^$/d' > 4-password.txt
