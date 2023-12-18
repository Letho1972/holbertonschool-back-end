#!/usr/bin/env python3

""" Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        # Fetch employee information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task['title']
                           for task in todos_data if task["completed"]]

        # Display TODO list progress
        total_tasks = len(todos_data)
        completed_tasks_count = \
            sum(1 for task in todos_data if task["completed"])

        print("Employee {} is done with tasks ({}/{}):"
              .format(employee_name, completed_tasks_count, total_tasks))

        # Display titles of completed tasks
        for task_title in completed_tasks:
            print("    {}".format(task_title))

    except requests.RequestException as e:
        print("Error fetching data: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
