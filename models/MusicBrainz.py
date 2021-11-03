import musicbrainzngs


class MusicBrainz:
    musicbrainzngs.set_useragent("Music enthusiast app", "1.0", "ghezo96@gmail.com")

    def __init__(self, artist_name):
        musicbrainzngs.set_format(fmt="json")
        self.artist = artist_name

    def get_artist(self, artist_name):
        result = musicbrainzngs.search_artists(artist=self.artist, limit="3")
        return result['artist-list']