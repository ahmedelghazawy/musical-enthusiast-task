import json
import re


def cleanup_lyrics(raw_lyrics, artist_name, song_name):
    phrase_to_remove = "paroles de la chanson " + song_name.lower() + " par " + artist_name.lower()
    pattern = '[^a-z\']|[\s+]'

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
