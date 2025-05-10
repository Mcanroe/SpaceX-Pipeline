import requests

url = "https://lldev.thespacedevs.com/2.3.0/launches/"
response = requests.get(url)
data = response.json()

print(response)
print(data)