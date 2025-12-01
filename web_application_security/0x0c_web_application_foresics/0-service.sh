#!/bin/bash
cat auth.log | awk '{print $5" "$6}' | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n 20
