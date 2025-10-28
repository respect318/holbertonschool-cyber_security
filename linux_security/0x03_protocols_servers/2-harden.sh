#!/bin/bash
find / -type f -perm -0002 -exec grep -l 'searchstring' {} \; 2>/dev/null

