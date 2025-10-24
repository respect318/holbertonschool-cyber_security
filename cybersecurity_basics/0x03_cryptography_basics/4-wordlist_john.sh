#!/bin/bash
john --show "$HASHFILE" | awk -F: '/:/{print $2}' | sed '/^$/d' > 4-password.txt
