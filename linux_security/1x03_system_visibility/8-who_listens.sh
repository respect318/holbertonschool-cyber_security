#!/bin/bash
lsof -i :"$1" | awk 'NR==2 {print $1}'
