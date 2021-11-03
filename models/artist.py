class Artist():
    def __init__(self, name="", artist_type="", gender="", country="", tags=[]):
        self.name = name
        self.artist_type = artist_type
        self.gender = gender
        self.country = country
        self.tags = tags

    def print_artist(self):
        artist = "Artist name: " + self.name + \
            "\nArtist type: " + self.artist_type + \
            "\nArtist gender: " + self.gender + \
            "\nArtist country: " + self.country + \
            "\nTags: " + str(self.tags)
        print(artist)