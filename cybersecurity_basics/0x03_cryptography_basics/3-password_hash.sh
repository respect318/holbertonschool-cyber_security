#!/bin/bash
SALT=$(openssl rand -hex 16) && echo -n "$1$SALT" | openssl dgst -sha512 > 3_hash.txt
