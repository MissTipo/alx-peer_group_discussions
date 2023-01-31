#!/usr/bin/python3
"""Returns subscriber count for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscriber given a subreddit"""
    BASE_URL = 'https://api.reddit.com'
    headers = {
        "User-Agent": "ChangeMeClient/0.1 by kolaoba"
    }
    res = requests.get("{}/r/{}/about".format(BASE_URL, subreddit),
                       headers=headers)
    if res.status_code == 404:
        return 0
    return res.json().get('data').get('subscribers')
