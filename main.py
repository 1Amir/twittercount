#Errors are still in the code
import json
import tweepy
from tweepy import OAuthHandler
 
apiad = ('https://twitter.com/realDonaldTrump')
 
auth = OAuthHandler(apiad)
 
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
