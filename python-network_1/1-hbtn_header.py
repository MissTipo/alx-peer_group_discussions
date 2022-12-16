#!/usr/bin/python3
"""
Send a request to a URL and displays the value of X-Request_Id variable
in the header response
"""
import urllib.request
import sys

arg = sys.argv
if __name__ == '__main__':
    url = arg[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        data = dict(response.headers)
        print(data['X-Request-Id'])
