#!/bin/bash
python3 -c "from base64 import b64decode; print(bytes(byte ^ 0x35 for byte in b64decode('$1'.replace('{xor}', ''))).decode('utf-8'))"
