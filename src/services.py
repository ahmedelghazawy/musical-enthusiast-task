import json
import requests
from models import *

import musicbrainzngs as mb


class ArtistService:
    mb.set_useragent("Music enthusiast app", "1.0", "ghezo96@gmail.com")

    def __init__(self, artist):
        mb.set_format(fmt="json")
        self.artist = artist

    def get_artist(self):
        result = mb.search_artists(artist=self.artist.name, limit="1")
        # artist = Artist()
        return result['artists'][0]

    def get_songs(self):
        works = mb.search_works(arid=self.artist.id, limit=300)
        song_list = []
        for song in works['works']:
            song_list.append(song['title'])
        return song_list


class SongService:

    def __init__(self, song):
        self.base_url = "https://api.lyrics.ovh/v1/"
        self.song = song

    def get_song_lyrics(self, artist, song_name):
        request_url = self.base_url + artist.name + song_name
        try:
            response = requests.get(request_url)
            if response.status_code == 200:
                song = Song(song_name, response.body['lyrics'], 0)
            else:
                return
        except requests.exceptions.Timeout:
            return

        except requests.exceptions.TooManyRedirects:
            print("Too many redirects")
            return
        except requests.exceptions.RequestException:
            return

    def count_lyrics(self):
        pass

