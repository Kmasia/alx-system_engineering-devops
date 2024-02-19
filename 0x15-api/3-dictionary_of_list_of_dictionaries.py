#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)


0x15-api/3-dictionary_of_list_of_dictionaries.py

#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch the list of all users (employees)
    users = requests.get(url + "users").json()

    # Create a dictionary containing to-do list information of all employees
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

