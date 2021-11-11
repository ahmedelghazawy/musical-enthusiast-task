import argparse
import warnings

from services import *

# Suppressing warnings given by the libraries used
warnings.filterwarnings("ignore")

# Adding command line arguments
parser = argparse.ArgumentParser(description="A program that counts average words in songs by artists.")
parser.add_argument('-f', '--file', required=False, action="store_true", dest="file",
                    help="Generates a CSV file containing number of words in each song by artist.")
args = parser.parse_args()

if __name__ == '__main__':

    artist_name = input("Please insert artist name\n")
    artist = Artist(artist_name)

    print("Thanks, please hang tight while we find this artist.\n")
    artist_service = ArtistService(artist)
    artist = artist_service.get_artist()

    # In case wrong artist name was given, or artist couldn't be found
    if artist == None:
        print("Artist not found, please try again")
        exit(0)
    else:
        print("Great news! We found the artist, one moment while we gather their information.\n")

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

    print("Counting their songs.\n")
    artist.songs = artist_service.get_songs()
    artist.print_artist()

    print("Counting words in songs' lyrics.\n")
    for i in range(len(artist.songs)):
        song_service = SongService(artist.songs[i])
        current_song = song_service.get_song_lyrics(artist)
        artist.songs[i] = current_song

    average_words = lyrics_counter(artist.songs)

    print("Average number of words per song: " + str(average_words) + ".\n")

    if args.file:
        print("Writing data into file.\n")
        generate_song_csv(artist)
