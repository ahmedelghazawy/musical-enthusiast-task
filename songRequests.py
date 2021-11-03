import models.Artist as Artist
import models.MusicBrainz as mb
artist_name = input("Please insert artist name\n")

artist = mb.MusicBrainz(artist_name)
query_result = artist.get_artist()

# for artist in query_result:
#     print(artist)
#     print()
artist_list = []
for artist in query_result:
    artist_list.append(Artist.Artist(artist['id'], artist['name'], artist['type'], artist['country']))

for artist in artist_list:
    artist.print_artist()
