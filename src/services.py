import json
import requests
from src.models import *

import musicbrainzngs as mb


class ArtistService:
    mb.set_useragent("Music enthusiast app", "1.0", "ghezo96@gmail.com")

    def __init__(self, artist_name):
        mb.set_format(fmt="json")
        self.artist = artist_name

    def get_artist(self):
        result = mb.search_artists(artist=self.artist, limit="3")
        # artist = Artist()
        return result['artists']


class LyricsService:

    def __init__(self):
        pass

    def count_lyrics(self, lyrics):
        pass


class SongService:

    def __init__(self):
        base_url = "https://api.lyrics.ovh/v1/"

    def get_song_lyrics(self, artist, song_name):
        request_url = self.base_url + artist.name + song_name
        try:
            response = requests.get(request_url)
            if response.status_code == 200:
                song = Song.Song(song_name, response.body, 0)
            else:
                return
        except requests.exceptions.Timeout:
            return

        except requests.exceptions.TooManyRedirects:
            print("Too many redirects")
            return
        except requests.exceptions.RequestException:
            return
