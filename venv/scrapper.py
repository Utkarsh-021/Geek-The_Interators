import bs4
import requests


import requests
URL = "https://www.apollohospitals.com/"
r = requests.get(URL)
print(r.content)