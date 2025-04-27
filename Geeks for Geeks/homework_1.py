import requests
response = requests.get('https://pypi.org/project/pip')
print(response.text)