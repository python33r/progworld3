# Finds artists with >10 plays on BBC radio stations in the past week
# (Simpler version, using Requests)
# See http://blog.efford.org/prog-world-part3.html

import requests

feed_url = "http://www.bbc.co.uk/programmes/music/artists/charts.json"

# Access data feed and deserialize JSON data

response = requests.get(feed_url)
data = response.json()

# Search list of artists for play counts > 10

artists = data["artists_chart"]["artists"]

for artist in artists:
    if artist["plays"] > 10:
        print(artist["name"], artist["plays"])
