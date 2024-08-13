#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """

    headers = {'User-Agent': 'my-app/0.0.1'}

    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        
        response = requests.get(url, headers=headers, allow_redirects=False)

    
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0

