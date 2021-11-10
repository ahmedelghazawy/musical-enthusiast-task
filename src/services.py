import json
import requests
from models import *
from helper_functions import *

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
        song_list = []
        for offset in range(0, 1000, 100):
            works = mb.search_works(arid=self.artist.id, limit=100, offset=offset)
            for song in works['works']:
                current_song = Song(song['title'], "", 0)
                song_list.append(current_song)
        return song_list


class SongService:

    def __init__(self, song):
        self.base_url = "https://api.lyrics.ovh/v1/"
        self.song = song

    def get_song_lyrics(self, artist):
        request_url = self.base_url + artist.name + "/" + self.song.name
        try:
            response = requests.get(request_url)
            if response.status_code == 200:
                lyrics = cleanup_lyrics(response.content, self.song.name)
                self.song.lyrics = lyrics
                return self.song
            else:
                return self.song
        except requests.exceptions.Timeout:
            return

        except requests.exceptions.TooManyRedirects:
            print("Too many redirects")
            return
        except requests.exceptions.RequestException:
            return

    def count_lyrics(self):
        pass

