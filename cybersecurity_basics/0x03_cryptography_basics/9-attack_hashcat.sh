#!/bin/bash
hashcat -m 0 -a 1 $1 $2 $3  > 9-password.txt
