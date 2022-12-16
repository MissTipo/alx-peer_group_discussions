#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status using request package
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t - type: {}" .format(type(r.text)))
    print("\t - content: {}" .format(r.text))
