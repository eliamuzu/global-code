from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY= os.getenv('API_KEY')

import requests

r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}")
pprint(r.json())
