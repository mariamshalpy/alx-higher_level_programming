#!/bin/bash
# curl OPTIONS
curl -sIX "OPTIONS" "$1" | grep "Allow" | cut -d\  -f2-9
