# Computes depth statistics for recent M4.5+ earthquakes
# Note: requires Python 3.4 due to use of statistics module
# See https://nickefford.silvrback.com/programming-the-world-3

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

reader = csv.reader(text.splitlines())

# Read column headings (which are not used here)

headings = next(reader)

# Fetch each record and collect depths into a list

depths = []
for record in reader:
    # Depth is fourth value, at index 3
    # Value is a string and must be converted to a float
    depth = float(record[3])
    depths.append(depth)

# Compute mean & standard deviation of depths

mean = statistics.mean(depths)
stdev = statistics.stdev(depths, mean)

print("Mean    = {:.1f} km".format(mean))
print("Std dev = {:.1f} km".format(stdev))
