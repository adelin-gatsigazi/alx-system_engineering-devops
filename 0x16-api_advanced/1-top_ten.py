#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to get the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, print None.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "python:subreddit.hot.posts:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            for post in posts:
                print(post['data'].get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)

