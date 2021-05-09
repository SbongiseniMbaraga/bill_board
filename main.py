import requests
import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "11548843d95b47f39a773c62aed14603"
SPOTIPY_CLIENT_SECRET = "216833cab5ed4cd8b0dd1e395ac5af5b"

#convert user string to date format
user_input = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:")
formatted_to_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")
date = formatted_to_date.date()

#add user date to url to get specific top songs during that date
URL = "https://www.billboard.com/charts/hot-100/" + str(date)
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

#check date
date_button = soup.find_all(name="button", class_="date-selector__button button--link")

for button_date in date_button:
    date_spaces = button_date.text
    date_no_spaces = date_spaces.strip()
    print(date_no_spaces)

#gets the song title based on the user date and add to list
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

Top_100_songs = []
for song in all_songs:
    song_title = song.text
    Top_100_songs.append(song_title)

#Spotify Authentication



