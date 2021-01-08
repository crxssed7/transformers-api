import requests

BASE = "http://127.0.0.1:5000/"

data = {
    'name': 'Test',
    'allegiance': 1,
    'subgroup': 1,
    'role': 'Role',
    'first_appearance': 'yeet',
    'image': 'yeet',
    'description': 'This is a really long description'
}

response = requests.get(BASE + "transformers/1")
print(response.json())