import requests

API_KEY =   # you can get your API_KEY on setlist.fm web page...

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

data = response.json()['setlist'][0]['sets']['set']
songsData = data[0]['song']
try:  # try method if setlist has encore songs, if it has them, it appends them to a setlistAll list
    songsData2 = data[1]['song']
    rangeSong = len(songsData)
    rangeEncore = len(songsData2)
    rangeAll = rangeEncore + rangeSong
    setlistAll = []
    for num in range(rangeSong):
        setlistAll.append(songsData[num]['name'])

    for num in range(rangeEncore):
        setlistAll.append(songsData2[num]['name'])
    print(setlistAll)
except IndexError:  # if an error is raised because there are no encore songs, only songs are passed to setlistAll list
    rangeSong = len(songsData)
    setlistAll = []
    for num in range(rangeSong):
        setlistAll.append(songsData[num]['name'])
    print(setlistAll)


