#!/usr/bin/python3
"""Returns titles of all hot articles for a given subreddit"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Return titles of all hot articles given a subreddit"""
    BASE_URL = 'https://api.reddit.com'
    headers = {
        "User-Agent": "ChangeMeClient/0.1 by kolaoba"
    }
    params = {
        "after": after,
        "count": count
    }
    res = requests.get("{}/r/{}/hot".format(BASE_URL, subreddit),
            headers=headers, params=params)
    if res.status_code == 404:
        return None
    data = res.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    children = res.json().get('data').get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    return hot_list
