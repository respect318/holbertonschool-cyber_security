#!/bin/bash
lsb_release -i | cut -d':' -f2 | xargs

