#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and print
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints None if the subreddit is invalid or an error occurs.
    """
    headers = {
        'User-Agent': 'Python/requests:subreddit.top_ten:v1.0.0 (by /u/your_username)'
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data')
        if not data:
            print(None)
            return

        posts = data.get('children', [])
        for post in posts:
            print(post['data'].get('title'))

    except requests.RequestException:
        print(None)

