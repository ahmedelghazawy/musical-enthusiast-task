import requests
import json
import musicbrainzngs

headers = {"Accept": "application/json"}
query = {"query": "rihanna"}
response = requests.get("https://musicbrainz.org/ws/2/artist/", headers=headers, params=query)

for artist in response.json()['artists']:
    print()
    print(artist)
    print()
