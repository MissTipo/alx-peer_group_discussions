#!/usr/bin/python3
"""
Takes GitHub credentials(username and password) and uses the GitHub API
to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    r = requests.get(
            'https://api.github.com/user',
            auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    try:
        r_dict = r.json()
        print(r_dict['id'])
    except KeyError:
        print("None")
