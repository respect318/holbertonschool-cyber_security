#!/bin/bash
sudo nmap -p http,https,ftp,ssh,telnet -sM --vv $1
