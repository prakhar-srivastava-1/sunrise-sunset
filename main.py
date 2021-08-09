import requests

MY_LAT = 22.171841
MY_LONG = 76.065422

params = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
response_data = response.json()
print(f"Time of Sunrise - {response_data['results']['sunrise']}")
print(f"Time of Sunset - {response_data['results']['sunset']}")
