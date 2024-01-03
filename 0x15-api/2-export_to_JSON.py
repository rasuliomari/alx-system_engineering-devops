#!/usr/bin/python3
# Using what you did in the task #0, extend your Python
# script to export data in the JSON format.

import json
from requests import get
from sys import argv


# A function to fetch data from the REST API and export it as JSON
def api_to_json(user_id):
    # Create an empty list to store task information
    task_list = []
    
    # Define the base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information using the provided user_id
    user = get(url + "users/{}".format(user_id)).json()
    
    # Fetch tasks associated with the user
    tasks = get(url + "todos?userId={}".format(user_id)).json()
    
    # Iterate through the tasks and create dictionaries for each task
    for task in tasks:
        tdict = {}
        tdict["task"] = task.get("title")
        tdict["completed"] = task.get("completed")
        tdict["username"] = user.get("username")
        task_list.append(tdict)
    
    # Open a JSON file with the user_id as the filename and write the data
    with open("{}.json".format(user_id), 'w', newline='') as json_file:
        json.dump({argv[1]: task_list}, json_file)


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the api_to_json function with the user ID
    # provided as a command-line argument
    api_to_json(int(argv[1]))
