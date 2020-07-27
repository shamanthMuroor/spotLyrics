"""
    * Displays the lyrics of the song being played in spotify
    * Uses spotify api to get the current playing song and artist of that song
    * Uses genius.com api to get and display the lyrics
    * If genius.com api fails, then searches google for the lyrics of song! 
"""

import spotipy
import spotipy.util as util
from config import USERNAME, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, TOKEN
import requests
from bs4 import BeautifulSoup
import sys
import time
import webbrowser
import re

def get_current_song_details(spot_token):
    """ This funtion gets the details of currently playing song through spotify api """
    #Create a Spotify() instance
    sp = spotipy.Spotify(auth=spot_token)
    # method currently playing return actual song on Spotify
    try:
        current_song = sp.currently_playing()
        # Extract artist from json response
        artist = current_song['item']['artists'][0]['name']
        # Extract song name from json response
        song_name = current_song['item']['name']
        song_name = re.search(r'^[\w ]+', song_name)
        print('\nSong: {}\nArtist: {}'.format(song_name[0], artist))
        return song_name[0], artist
    except:
        print("No song is being played")
        sys.exit(1)

def get_genius_song_lyrics(song_name, artist):
    """ This funtion gets the song lyrics from genius.com using their api """
    base_url = "http://api.genius.com"
    headers = {'Authorization': 'Bearer {}'.format(TOKEN)}
    search_url = base_url + "/search"
    params = {'q': song_name}
    response = requests.get(search_url, params=params, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist:
            song_info = hit
            break

    if song_info:
        # Get lyrics by scrapping website
        song_path = song_info["result"]["url"]
        print(song_path)
        res = requests.get(song_path)
        if res.status_code == 200:
            time.sleep(2)
            # BeautifulSoup library return an html code
            html_code = BeautifulSoup(res.text, features="html.parser")
            time.sleep(8)
            # Extract lyrics from beautifulsoup response using the correct prefix {"class": "lyrics"}
            lyrics = html_code.find("div", {"class": "lyrics"}).get_text()
            print(lyrics)
            ex = input("\n\nEnter any key to exit!")
            return 1
    return 0


scope = 'user-read-currently-playing'
spot_token = util.prompt_for_user_token(USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
if spot_token:
    # Get details of currently playing song through spotify api
    song_name, artist = get_current_song_details(spot_token)

    # Get song lyrics from genius.com using their api
    result = get_genius_song_lyrics(song_name, artist)
    if not result:
        print("Couldn't find lyrics in genius.com, opening google chrome search")
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = "https://www.google.com/search?q={}+{}+lyrics".format(song_name,artist)
        webbrowser.get(chrome_path).open(url)
    sys.exit(0)
else:
    print("Can't get token for ", USERNAME)
    sys.exit(1)
