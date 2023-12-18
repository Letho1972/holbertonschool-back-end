#!/usr/bin/python3

""" Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todos_data if task["completed"]]

        # Display TODO list progress
        total_tasks = len(todos_data)
        completed_tasks_count = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks\
               ({completed_tasks_count}/{total_tasks}):")
        print(f"\t{employee_name}: {completed_tasks_count}\
               completed tasks out of {total_tasks}")

        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
