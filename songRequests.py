import requests
import json
from models import artist
# import musicbrainzngs
artist_name = input("Please insert artist name\n")
headers = {"Accept": "application/json"}
query = {"query": artist_name}
response = requests.get("https://musicbrainz.org/ws/2/artist/", headers=headers, params=query)

# print(response.text)
response_text = json.loads(response.text)
# artists = response_text['artists']
# print(artists)
artist_list = []
for current_artist in response_text['artists']:
    keys = current_artist.keys()
    name = ""
    artist_type = ""
    country = ""
    gender = ""
    tags = []
    if 'type' in keys:
        artist_type = current_artist['type']
    if 'gender' in keys:
        gender = current_artist['gender']
    if 'name' in keys:
        name = current_artist['name']
    if 'country' in keys:
        print("Artist country: " + current_artist['country'])
    if 'tags' in keys:
        for tag in current_artist['tags']:
            if tag['count'] > 0:
                tags.append(tag['name'])
    artist_list.append(artist.Artist(name, artist_type, gender, country, tags))

for entry in artist_list:
    entry.print_artist()
    print()
