import requests

url = 'https://api.example.com/data'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print(response.json())  # Use .json() to parse JSON responses
else:
    print(f"Error: {response.status_code}")