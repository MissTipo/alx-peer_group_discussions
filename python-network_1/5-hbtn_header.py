#!/usr/bin/python3
"""
Send a request to the URL and send a request to the URL to display the value
of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except KeyError:
        pass
