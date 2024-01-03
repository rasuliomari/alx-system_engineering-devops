#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
from requests import get
from sys import argv


# A function to retrieve data from the API and export to CSV
def api_to_csv(user_id):
    # Define the base URL of the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Make an API request to fetch user information
    user = get(url + "users/{}".format(user_id)).json()

    # Make an API request to fetch the user's TODO list
    tasks = get(url + "todos?userId={}".format(user_id)).json()

    # Open a CSV file for writing, using the user_id as the filename
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        file_stream = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the CSV file with relevant data
        for task in tasks:
            file_stream.writerow([user_id, user.get("username"),
                                  task.get("completed"),
                                  task.get("title")])


# Check if the script is run as the main program
if __name__ == "__main__":
    # Parse the command-line argument as the user_id
    api_to_csv(int(argv[1]))
