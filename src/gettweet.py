import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from getmyapi import GetAPI
__author__ = 't35khan'

consumer_key = GetAPI.getapi('consumer_key')
consumer_secret = GetAPI.getapi('consumer_secret')
access_token = GetAPI.getapi('access_token')
access_secret = GetAPI.getapi('access_secret')

	
class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            print(raw_data)
            with open ("../input/twitDB.txt",'a') as txtfile:
                txtfile.write(raw_data)
            return True
        except BaseException as e:
            print('Failed ondata',str(e))
            time.sleep(10)

    def on_error(self, status_code):
        print(status_code)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["syria" or "refugee" or "syrian" or "migrant crisis"])