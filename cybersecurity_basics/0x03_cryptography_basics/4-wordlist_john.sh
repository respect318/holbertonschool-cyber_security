#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-MD5 $1 | cut -d ' ' -f 1,2,3 > 4-password.txt
