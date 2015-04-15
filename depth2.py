# Computes depth statistics for recent M4.5+ earthquakes
# (Alternate version, using DictReader and list comprehensions)
# Note: requires Python 3.4 due to use of statistics module
# See http://blog.efford.org/prog-world-part3.html

import csv
import statistics
from urllib.request import urlopen

# Construct feed URL for M4.5+ quakes in the past 7 days

base = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
feed_url = base + "4.5_week.csv"

# Open URL and read text from it

source = urlopen(feed_url)
text = source.read().decode()

# Create reader for the dataset

reader = csv.DictReader(text.splitlines())

# Extract depths into a list

depths = [ float(record["depth"]) for record in reader ]

# Compute mean & standard deviation of depths

mean = statistics.mean(depths)
stdev = statistics.stdev(depths, mean)

print("Mean    = {:.1f} km".format(mean))
print("Std dev = {:.1f} km".format(stdev))
