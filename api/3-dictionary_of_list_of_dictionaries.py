#!/usr/bin/python3

""" Extend your Python script to export data in the JSON format. """

import requests
import sys
import json


def to_do(employee_ID):
    """
    Retrieve employee information
    and TODO list progress based on the employee ID.

    Args:
        employee_ID (int): The ID of the employee.

    Returns:
        dict: Dictionary containing employee information
          and TODO list progress.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_name = employee_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code == 200:
        total_tasks = len(todos_data)
        completed_tasks = 0

        for task in todos_data:
            completed_tasks += task['completed']

        employee_info = {
            "username": employee_name,
            "tasks": [{"task": task['title'], "completed": task['completed']}
                      for task in todos_data]
        }

        return employee_info


if __name__ == "__main__":
    all_employees_data = {}

    if len(sys.argv) != 1:
        print("Usage: python script.py")
        sys.exit(1)

    for employee_id in range(1, 11):  # Assuming employee IDs from 1 to 10
        employee_data = to_do(employee_id)
        if employee_data:
            all_employees_data[employee_id] = employee_data

    # Export data to JSON file
    output_file = "todo_all_employees.json"
    with open(output_file, 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)

    print(f"Data exported to {output_file}")
