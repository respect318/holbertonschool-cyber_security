#!/bin/bash
sudo nmap -sn -PS 20,80,443 $1
