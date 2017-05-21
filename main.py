import json
import tweepy
from tweepy import OAuthHandler
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
callbackurl = 'https://twitter.com/settings/devices?success=true'
consumer_key = 'NYQJgVDpiJJZ92bGeFJ3QWopg'
consumer_secret = 'EJ6cPG4Itr1jk3gn4raIBwZdXvK0afS65fC5VK5V53pTdocXgt'
access_token = '865405999041044481-GMDNMBwY4zKAgR2mY7xGNAUqFcH2Tdh'
access_secret = 'D5zp2ZCst0bRNjHAxvypRb7CHTuks9iNedz5TF4vwzR9L'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,callbackurl)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline).items():

    this = tweet.text
    print this
    this = this.split()
    amountwords = len(this)
    print "word count:",amountwords
