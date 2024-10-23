import requests

request = "https://api.chucknorris.io/jokes/random"

try:
  response = requests.get(request)
  if response.status_code == 200:
      json_data = response.json()
      print(json_data['value'])

except requests.exceptions.RequestException as e:
    print("Request failed")


