#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys
arg = sys.argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(arg) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json['id'], r_json['name']))
        elif r_json == {}:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
