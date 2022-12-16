#!/usr/bin/python3
"""
Send a POST request to the passed URL with an email as a parameter
"""
import urllib.request
import urllib.parse
import sys

arg = sys.argv
if __name__ == "__main__":
    url = arg[1]
    value = {}
    value['email'] = arg[2]
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
