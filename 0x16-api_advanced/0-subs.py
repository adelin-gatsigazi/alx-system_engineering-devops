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
        if response.status_code == 200:#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0

