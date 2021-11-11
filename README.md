# Musical enthusiast task

---

## Overview

### Description:
An application that uses free online services to acquire musician details, then count average number of words 
used in their songs. This project is following the PEP8 standards for python formatting.

### APIs used:
1. [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API): Used for acquiring artist name,
ID and names of songs by them.
2. [Lyrics.ovh](https://lyricsovh.docs.apiary.io/): Used for acquiring song lyrics.

### Main python libraries used:
1. Argparse
2. CSV
3. JSON
4. MusicBrainzngs
5. Requests

---

## Installation and running

### Installation

**Prerequisites: *python3* and *venv* .**

First things first, make sure you have your environment set up.
Start by creating a python 3 virtual environment as follows:

`python3 venv env/`

Next, you should install all the packages mentioned in [requirements.txt](./src/requirements.txt), as it lists the packages in a pip-ready format.

`source env/bin/activate`

`pip3 install requirements.txt`

After this step, you should check and validate that all the packages have been installed.

`pip3 freeze`

Now you're all set to go.

### Running

Open a terminal window inside your project root directory, then do the following.

`source env/bin/activate` *only if virtual environment wasn't already running.*

`cd src`

`python3 app.py -h`

This last command should show you what the app is, 
and what the options are to print the words in each song into an external csv file.
After this, follow the prompts on the screen.

---

## Limitations

1. The lyrics API would send the data including unexpected parts, 
such as additional artist names before they say something, or background noise description,
ect. This means the word count isn't always 100% accurate, but for artists with more songs,
this should have a lower effect on averages.
2. The song API sometimes doesn't have the lyrics to some songs, so that might affect the averages.
3. The artist/song API might have the artists under different names, or include some of their data
under the separate entity, meaning not all of their works may be displayed. Another issue with it is that 
some song names might be written in emojis or unreadable characters, so the songs wouldn't be accepted easily.

---

## To be added in future updates

1. A local database to include data from previous queries, hence reducing the 
number of requests over the API.
2. Linking artists' data with the ones falling under different artists' data
(e.g: after group breaking up, different stage name, features, etc.).