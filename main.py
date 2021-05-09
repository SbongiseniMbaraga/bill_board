import requests
import datetime
from bs4 import BeautifulSoup

#convert string to date formate
user_input = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:")
formatted_to_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")
date = formatted_to_date.date()

URL = "https://www.billboard.com/charts/hot-100/2000-08-12"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")


#gets the song title in the correct
for song in all_songs:
    song_title = song.text
    print(song_title)
