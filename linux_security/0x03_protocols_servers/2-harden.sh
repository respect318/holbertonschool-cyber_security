#!/bin/bash
world_writable_dirs=$(find / -type d -perm -0002 2>/dev/null)
