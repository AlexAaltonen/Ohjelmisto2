import requests
# dbe344fcfb50969aee786a14e9eecd3d

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
hakusana = input("Anna kaupunki: ")


# geoping http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=5&appid=dbe344fcfb50969aee786a14e9eecd3d"
vastaus = requests.get(pyyntö).json()

print(vastaus)