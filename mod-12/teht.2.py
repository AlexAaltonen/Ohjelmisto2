import requests
import json
API_KEY = "dbe344fcfb50969aee786a14e9eecd3d"

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
hakusana = input("Anna kaupunki: ")


# geoping http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=5&appid=dbe344fcfb50969aee786a14e9eecd3d"
vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()


lat = json_vastaus[0]["lat"]

lon = json_vastaus[0]["lon"]


pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

vastaus2 = requests.get(pyyntö2)
json_vastaus2 = vastaus2.json()

#print(json_vastaus2)
#print()

#print(json_vastaus2["weather"][0]["main"])
#print(json_vastaus2["main"])
#print(json_vastaus2["main"]["temp"])

saa = json_vastaus2["weather"][0]["main"]

lampotila = json_vastaus2["main"]["temp"]

print(f"Sää: {saa}")

print(f"Lämpötila: {lampotila}")
