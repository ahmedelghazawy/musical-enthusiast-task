from models import *
from services import *
import sys

artist_name = ""
if len(sys.argv) > 1:
    artist_name = sys.argv[1]
else:
    artist_name = input("Please insert artist name\n")
artist = Artist(artist_name)

artist_service = ArtistService(artist)
artist = artist_service.get_artist()

# for artist in query_result:
#     print(artist)
#     print()

artist_id = artist_name = artist_type = artist_country = ""
keys = artist.keys()
if "id" in keys:
    artist_id = artist['id']
if "name" in keys:
    artist_name = artist['name']
if "type" in keys:
    artist_type = artist['type']
if "country" in keys:
    artist_country = artist['country']
artist = Artist(artist_name, artist_id, artist_type, artist_country)
artist_service.artist = artist

# for artist in artist_list:
artist.songs = artist_service.get_songs()
artist.print_artist()
print("Names of songs by this artist\n")
for song in artist.songs:
    print(song)