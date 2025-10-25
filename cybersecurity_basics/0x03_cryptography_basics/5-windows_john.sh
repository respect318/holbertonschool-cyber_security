#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=NT "$1"| cut -d ' ' -f 2 >5-password.txt
