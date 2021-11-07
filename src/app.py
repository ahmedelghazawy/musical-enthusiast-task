from models import *
from services import *

artist_name = input("Please insert artist name\n")

artist_service = ArtistService(artist_name)
query_result = artist_service.get_artist()

# for artist in query_result:
#     print(artist)
#     print()
artist_list = []
for artist in query_result:
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
    artist_list.append(Artist(artist_id, artist_name, artist_type, artist_country))

for artist in artist_list:
    artist.print_artist()
