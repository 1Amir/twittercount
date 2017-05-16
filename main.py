#code has not been tested as I have not been able to download the import tweepy.
import json
import tweepy
from tweepy import OAuthHandler
auth = OAuthHandler(https://twitter.com/realDonaldTrump)  
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
