#!/bin/bash
nmap -p 111,2049 --script=nfs-ls "192.168.1.100"
