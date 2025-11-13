#!/bin/bash
sudo nmap -sX -p [440-450]  $1 --open --packet-trace --reason
