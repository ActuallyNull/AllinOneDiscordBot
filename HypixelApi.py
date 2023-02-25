import requests
import os
from dotenv import load_dotenv
# Replace YOUR_API_KEY with your actual API key
load_dotenv()
api_key = os.getenv("API_KEY")
uuid = os.getenv("UUID")
profileID = os.getenv("PROFILE_ID")
# Set the player name to the desired username
player = 'ActuallyNull'

# Make the request to the API
url = 'https://api.slothpixel.me/api/skyblock/calendar'

def apiRequestSpecific(param):
    response = requests.get(url)
    data = response.json()
    return data[param]

def apiRequestGeneral():
    response = requests.get(url)
    data = response.json()
    return data




