import requests
response = requests.get("https://wikipedia.org/")
if response.status_code ==200:
    print("wiki page found")