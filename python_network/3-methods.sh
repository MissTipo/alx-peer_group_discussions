#!/usr/bin/env bash
# display content size using curl

curl -sI "$1" | grep -i 'allow' | cut -d " " -f2-
