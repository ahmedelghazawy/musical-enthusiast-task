class Artist():
    def __init__(self, artist_id, name, artist_type="", country=""):
        self.id = artist_id
        self.name = name
        self.artist_type = artist_type
        self.country = country

    def print_artist(self):
        artist = "ID: " + self.id + \
            "\nArtist name: " + self.name + \
            "\nArtist type: " + self.artist_type + \
            "\nArtist country: " + self.country
        print(artist)