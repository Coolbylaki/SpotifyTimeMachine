import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy import SpotifyOAuth

SPOTIFY_REDIRECT_URI = "https://example.com"
SPOTIFY_CLIENT_ID = os.environ.get("Spotify_id")
SPOTIFY_CLIENT_SECRET = os.environ.get("Spotify_secret")
BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"

# date_choice = input("Which year do you want to travel to?"
#                     "Type the date in this format YYYY-MM-DD: ")
date_choice = "2020-02-07"

response = requests.get(f"{BILLBOARD_ENDPOINT}/{date_choice}/")

billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")
songs = soup.select(selector="li h3#title-of-a-story")

top_100 = [song.getText().strip() for song in songs]

OAuth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                     client_secret=SPOTIFY_CLIENT_SECRET,
                     redirect_uri=SPOTIFY_REDIRECT_URI,
                     scope="playlist-modify-private",
                     show_dialog=True,
                     cache_path=".cache")

sp = spotipy.Spotify(auth_manager=OAuth)

user_id = sp.current_user()["id"]
