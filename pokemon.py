#!/usr/bin/env python3

import requests

URL = "https://pokeapi.co/api/v2/pokemon"

r = requests.get(URL)

j = r.json()

j['results'][0]
j['count']

# This was for testing


