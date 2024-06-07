#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0

