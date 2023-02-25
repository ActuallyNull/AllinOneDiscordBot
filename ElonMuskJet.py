import requests
import json

# Replace YOUR_ACCESS_KEY with your actual access key
access_key = "e0d9e3f83bf683e5ee87ad5a64fcfb22"
# Flight tracking endpoint
url = f"http://api.screenshotlayer.com/api/capture?access_key={access_key}&url=https%3A%2F%2Fglobe.adsbexchange.com%2F%3Ficao%3Da835af&fullpage=1&delay=10"

# Make the API request
response = requests.get(url)

# Get the flight data from the API response


# Print the flight data
def printData():
    print(response)

if __name__ == "__main__":
    printData()