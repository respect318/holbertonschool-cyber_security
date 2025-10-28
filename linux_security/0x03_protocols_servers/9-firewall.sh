#!/bin/bash
sudo iptables -L INPUT --line-numbers | wc -l
