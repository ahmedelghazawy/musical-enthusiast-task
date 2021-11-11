from models import *
from services import *
from helper_functions import lyrics_counter
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

artist.songs = artist_service.get_songs()
artist.print_artist()


for i in range(len(artist.songs)):
    song_service = SongService(artist.songs[i])
    current_song = song_service.get_song_lyrics(artist)
    artist.songs[i] = current_song

average_words,average_distinct_words = lyrics_counter(artist.songs)

print("Average number of words per song: " + str(average_words))
print("Average distinct words per song: " + str(average_distinct_words))