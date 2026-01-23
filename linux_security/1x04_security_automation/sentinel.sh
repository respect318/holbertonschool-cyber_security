#!/bin/bash
CONFIG_FILE="./sentinel.conf"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "ERROR: Config file not found: $CONFIG_FILE" >&2
    exit 1
fi

source "$CONFIG_FILE"

if [ -z "${SERVICES+x}" ] || [ -z "${FILES_TO_WATCH+x}" ]; then
    echo "ERROR: Required variables are missing in config file" >&2
    exit 1
fi
