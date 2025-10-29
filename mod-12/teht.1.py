from signal import valid_signals

import requests


pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö)

json_vastaus = vastaus.json()

#print(json_vastaus)

print(json_vastaus["value"])