# Finds artists with >10 plays on BBC radio stations in the past week
# See https://nickefford.silvrback.com/programming-the-world-3

import json
from urllib.request import urlopen

feed_url = "http://www.bbc.co.uk/programmes/music/artists/charts.json"

# Open URL and read text from it

source = urlopen(feed_url)
text = source.read().decode()

# Deserialise the JSON data contained in the text

data = json.loads(text)

# Search list of artists for play counts > 10

artists = data["artists_chart"]["artists"]

for artist in artists:
    if artist["plays"] > 10:
        print(artist["name"], artist["plays"])
