#!/usr/bin/env bash
# display content size using curl
curl "$1"
echo " "
curl -sI "$1" | grep -i 'content-length'
echo " "
curl -sI "$1" | grep -i 'content-length' | cut -d " " -f1
# curl -s "$1" | wc -c
# curl -s "$1" | wc -c
