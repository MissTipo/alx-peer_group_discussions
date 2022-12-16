#!/usr/bin/python3
"""
Send a POST request to the passed URL with email as parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    print(r.text)
