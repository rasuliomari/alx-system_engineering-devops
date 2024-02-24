#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers.
"""

from requests import get


def number_of_subscribers(subreddit):
    """

    """
    headers = {"user-agent": "Vlone Me"}
    apiUrl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        data = get(apiUrl, headers=headers).json()
        count_subscribers = data["data"]["subscribers"]
        return (count_subscribers)
    except Exception:
        return 0
