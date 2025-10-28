#!/bin/bash
grep -E -v '^\s*#|^\s*$' "/etc/ssh/sshd_config"
