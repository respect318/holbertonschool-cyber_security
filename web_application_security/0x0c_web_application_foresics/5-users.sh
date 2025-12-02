#!/bin/bash
grep "new user: name=" auth.log | awk -F 'name=' '{print $2}' | awk -F ',' '{print $1}' | sort | uniq | paste -sd "," -
