#!/bin/bash
grep -E '^smtpd_tls_security_level' /etc/postfix/main.cf 2>/dev/null
