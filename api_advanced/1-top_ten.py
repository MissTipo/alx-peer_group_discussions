#!/usr/bin/python3
"""Returns first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """Return first 10 hot posts given a subreddit"""
    BASE_URL = 'https://api.reddit.com'
    headers = {
        "User-Agent": "ChangeMeClient/0.1 by kolaoba"
    }
    params = {
        "limit": 10
    }
    res = requests.get("{}/r/{}/hot".format(BASE_URL, subreddit),
                       headers=headers, params=params)
    if res.status_code == 404:
        return None
    children = res.json().get('data').get('children')
    print("\n".join([child.get('data').get('title') for child in children]))
