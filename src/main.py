__author__ = 't35khan'

from getcountry import GetCountry  as gc
from processtweets import ProcessTweets as pt
import csv
import os
import re
from string import punctuation

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
                    print("Using time zone to get country")
                    gapi_country = time_zone.split(" ")[-1]
                    gapi_country = (re.findall(r"[A-Za-z]",gapi_country))
                    gapi_country = "".join(gapi_country)
                    print(gapi_country)
                if gapi_country:
                    country = gapi_country
                    print(country)
                else:
                    country = "N/A"
            csvfile = open("../input/twitDB.csv","a")
            writer = csv.writer(csvfile,dialect='excel')
            writer.writerow([message,country])
            csvfile.close()
            tweet_count += 1
            print("tweets processed:",tweet_count)
