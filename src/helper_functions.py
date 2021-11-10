import json

def cleanup_lyrics(raw_lyrics):
    decoded_lyrics = raw_lyrics.decode('utf8')
    json_lyrics = json.loads(decoded_lyrics)
    clean_lyrics = json_lyrics['lyrics']
    # clean_lyrics = lyrics_dictionary['lyrics']
    return clean_lyrics
