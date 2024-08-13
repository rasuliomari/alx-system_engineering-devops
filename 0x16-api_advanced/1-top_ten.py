#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    # Reddit API URL for the first 10 hot posts in a subreddit
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid potential issues
    headers = {
        "User-Agent": "MyRedditBot/1.0 by Vlone Me"
    }

    try:
        # Send a GET request to the API without following redirects
        response = requests.get(api_url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data["data"]["children"]

            # Print the titles of the first 10 hot posts
            for post in range(len(hot_posts)):
                print(hot_posts[post]['data']['title'])
        else:
            print("None")  # Invalid subreddit or other issues
    except requests.exceptions.RequestException:
        print("None")  # Request-related error
