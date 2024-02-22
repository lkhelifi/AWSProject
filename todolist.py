import requests

# Replace 'YOUR_API_KEY' with your actual Todoist API key
api_key = 'YOUR_API_KEY'
base_url = 'https://api.todoist.com/rest/v1/'

# Get all tasks
def get_tasks():
    url = f'{base_url}tasks'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    tasks = response.json()
    return tasks

# Add a new task
def add_task(content):
    url = f'{base_url}tasks'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {'content': content}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
tasks = get_tasks()
print("Current tasks:")
for task in tasks:
    print(task['content'])

new_task_content = input("Enter a new task: ")
new_task = add_task(new_task_content)
print(f"Task '{new_task['content']}' added successfully!")
