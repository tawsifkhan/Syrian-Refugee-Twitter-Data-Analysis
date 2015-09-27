__author__ = 't35khan'

from getcountry import GetCountry  as gc
from processtweets import ProcessTweets as pt
import csv
import os

try:
    os.remove("../input/twitDB.csv")
except:
    pass

with open("../input/twitDB.txt",'r') as inputfile:
    for tweet in inputfile:
        if tweet != "\n":
            message,location,country,time_zone = pt.getdata(tweet)
            location = location.replace(" ","-")
            #print(location)
            #print(time_zone.split(" ")[-1])
            try:
                gapi_country = gc.getcountry(location)
                print(gapi_country)
            except:
                continue
            #print(gapi_country,country)
            if gapi_country:
                country = gapi_country
            else:
                gapi_country = time_zone.split(" ")[-1]
            csvfile = open("../input/twitDB.csv","a")
            writer = csv.writer(csvfile,dialect='excel')
            writer.writerow([message,country])
            csvfile.close()
