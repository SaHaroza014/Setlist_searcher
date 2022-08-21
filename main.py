import requests

API_KEY = "dT-x7DQsZ0yR2GwewRgEcUBvTGiS8zTVEVYE"

artist_name = input("Input artist name: ")
cityName = input("Input city name: ")
year = str(input("Input year: "))
url = f"https://api.setlist.fm/rest/1.0/search/setlists?artistName={artist_name}&cityName={cityName}&year={year}"
headers = {
    'Accept': 'application/json',
    "x-api-key": API_KEY
}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.status_code)


data = response.json()['setlist'][0]['sets']['set']
songsData = data[0]['song']
songsData2 = data[1]['song']
rangeSong = len(songsData)
rangeEncore = len(songsData2)
rangeAll = rangeEncore + rangeSong
print(rangeAll)
setlistAll = []
for num in range(rangeSong):
    setlistAll.append(songsData[num]['name'])

for num in range(rangeEncore):
    setlistAll.append(songsData2[num]['name'])

print(setlistAll)
