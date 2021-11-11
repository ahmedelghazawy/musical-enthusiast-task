class Artist:
    def __init__(self, name, artist_id="", artist_type="", country="", songs=[]):
        self.id = artist_id
        self.name = name
        self.artist_type = artist_type
        self.country = country
        self.songs = songs

    def print_artist(self):
        artist = "This artist is called " + self.name + \
                 ", they are a " + self.artist_type.lower() + \
                 ", they are from " + self.country + \
                 ", and have made " + str(len(self.songs)) + " songs\n"
        print(artist)


class Song:

    def __init__(self, name, lyrics, word_count=0):
        self.name = name
        self.lyrics = lyrics

    def print_song(self):
        print("Song name: " + self.name)
        print("Song lyrics: \n" + self.lyrics)
