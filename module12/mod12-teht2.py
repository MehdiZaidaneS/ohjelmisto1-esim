import requests



API_KEY = 'bbf31c251d7f39fa0c646765696b7839'

paikkakunta = input("Syöttä paikka kunta: ")

lat = ""
lon= ""

lonlat_request = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=5&appid={API_KEY}"

try:
    response = requests.get(lonlat_request)
    if response.status_code == 200:
        response_data = response.json()
        lat = response_data[0]['lat']
        lon = response_data[0]['lon']

except requests.exceptions.RequestException as e:
    print("Error!")


weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

try:
    response = requests.get(weather_request)
    if response.status_code == 200:
        response_data = response.json()
        temperature = response_data['main']['temp']
        print(f"{temperature - 273.15:.1f} celcius")
except requests.exceptions.RequestException as e:
    print("Error!")
