import requests
import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

#convert user string to date format
date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:")
formatted_to_date = datetime.datetime.strptime(date, "%Y-%m-%d")
date_2 = formatted_to_date.date()

#add user date to url to get specific top songs during that date
URL = "https://www.billboard.com/charts/hot-100/" + str(date_2)
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
song_names = [song.text for song in all_songs]
Top_100_songs.append(song_names)

# for song in all_songs:
#     song_title = song.text
#     Top_100_songs.append(song_title)

print(Top_100_songs)

#Spotify Authentication
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URL = "http://example.com "

credentials = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#search spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#create a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



