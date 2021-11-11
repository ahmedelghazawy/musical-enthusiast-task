import csv
import json
import re


def cleanup_lyrics(raw_lyrics, artist_name, song_name):
    # Most lyrics contain this French header, so it's being removed
    phrase_to_remove = "paroles de la chanson " + song_name.lower() + " par " + artist_name.lower()
    pattern = '[^a-z\']|[\s+]'

    # Lyrics are sent as a byte string, so the encoding and formatting and being changed to extract the lyrics
    decoded_lyrics = raw_lyrics.decode('utf8')
    json_lyrics = json.loads(decoded_lyrics)
    clean_lyrics = json_lyrics['lyrics'].lower()

    clean_lyrics = clean_lyrics.replace(phrase_to_remove, '')
    clean_lyrics = re.sub(pattern, ' ', clean_lyrics)
    clean_lyrics = re.sub("\s+n\s+", ' ', clean_lyrics)
    clean_lyrics = re.sub("\s+", " ", clean_lyrics)

    return clean_lyrics


def lyrics_counter(song_list):
    if len(song_list) == 0:
        return 0

    words_in_lyrics = {}

    for song in song_list:
        for word in song.lyrics.split(" "):
            if word in words_in_lyrics.keys():
                words_in_lyrics[word] += 1
            else:
                words_in_lyrics[word] = 1

    total_words = 0

    for word in words_in_lyrics.keys():
        total_words += words_in_lyrics[word]

    average_words = (total_words / len(song_list)) + 0.5

    return int(average_words)


def generate_song_csv(artist):
    if len(artist.songs) == 0:
        return 0

    words_in_songs = {}
    for song in artist.songs:
        number_of_words = len(song.lyrics.split(" "))
        words_in_songs[song.name] = number_of_words

    song_names = words_in_songs.keys()
    with open("../words_in_songs_by_" + artist.name.replace(" ", "_") + ".txt", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Song name", "Words"])

        for song in song_names:
            writer.writerow([song, words_in_songs[song]])
