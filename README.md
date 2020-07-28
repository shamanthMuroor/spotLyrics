# SpotiPy Lyrics 

Get the lyrics of currently playing song on Spotify. It used spotify web api to get the current playing song and gets the lyrics using API from genius.com. If genius.com doesn't have the song, then the lyrics will be searched in google.


## Installation(Pre-requisite)

```bash
pip install spotipy
pip install bs4
pip install requests
```

## Documentations

Spotipy's full documentation: http://spotipy.readthedocs.org/
Genius.com API documentation: https://docs.genius.com/
Spotify.com API documentation: http://developers.spotify.com/documentation/

## Getting started

* To get started, signup/login and create a new app on https://developers.spotify.com/
* USERNAME is your spotify username, you can get it in account section of spotify.
* You get your own new ID and SECRET codes, add those to separate file: config.py(*Not uploaded to github)
* SPOTIPY_REDIRECT_URI can be any url pointing to localhost, http://127.0.0.1/callback etc

* signup/login and create a new api client on https://genius.com/developers with your choice of entries.
* Redirect URI can be set to http://127.0.0.1:8080/callback itself
* Generate Access Token and get client access token, paste the code in config.py file against the TOKEN parameter. 

// Below would be an expected file of config.py
```python
USERNAME=''
SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='http://127.0.0.1:8080/callback'
TOKEN=''
```
 
## Backup search if genius.com doesn't have the song lyrics

* I have used chrome browser's path
* Check the chrome path, it may be different depending on the type of os

## Excecution

Run the python script!!!


### Queries

Please feel free to ask questions or correct me if i am wrong.
Suggestions are most welcome!
