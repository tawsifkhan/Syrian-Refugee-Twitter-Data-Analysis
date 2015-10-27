__author__ = 't35khan'

from getcountry import GetCountry  as gc
from processtweets import ProcessTweets as pt
import csv
import os

try:
    os.remove("../input/twitDB.csv")
except:
    pass
tweet_count = 0
with open("../input/twitDB.txt",'r') as inputfile:
    for tweet in inputfile:
        if len(tweet) > 1:
            message,location,country,time_zone = pt.getdata(tweet)
            location = location.replace(" ","-")
            if country == " ":
                try:
                    gapi_country = gc.getcountry(location)
                except:
                    gapi_country = time_zone.split(" ")[-1]
                if gapi_country:
                    country = gapi_country
                else:
                    country = "N/A"
            csvfile = open("../input/twitDB.csv","a")
            writer = csv.writer(csvfile,dialect='excel')
            writer.writerow([message,country])
            csvfile.close()
            tweet_count += 1
            print("tweets processed:",tweet_count)
