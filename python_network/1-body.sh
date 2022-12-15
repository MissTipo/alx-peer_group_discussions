#!/usr/bin/env bash
# display content size using curl
#curl -sI "$1" | grep -i 'content-length' | cut -d " " -f1

#result=$(curl -sI "$1" | grep -i 'HTTP/1.1' | cut -d " " -f2); if [ "$result" -eq 200 ]; then curl "$1"; fi

curl -sL "$1"
