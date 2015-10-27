__author__ = 't35khan'

import csv
class ProcessTweets:
    def getdata(tweet):
        try:
            message = tweet.split(",\"text\":\"")[1].split("\",")[0]
        except:
            return False
        try:
            location = tweet.split("\"location\":\"")[1].split("\",")[0]
        except:
            location = " "
        try:
            country = tweet.split("\"country\":\"")[1].split("\",")[0]
        except:
            country = " "
        try:
            time_zone = tweet.split("\"time_zone\":\"")[1].split("\",")[0]
        except:
            time_zone = " "

        return message,location,country,time_zone


