import random
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
#this function will make a random tweet made up of one of these letters.note:Sometimes it picks the same letter.
def maketweet():
    randomletters = random.choice(['a','b','c','d','e','f','g','h','i','t','v','W','X','w','x','z','y','B','U','Y'])
    random.shuffle(randomletters)
    tweetlist = randomletters
    random.choice(tweetlist)
    for line in tweetlist: 
        api.update_status(line)
        print line
        readtweet()
#this function will read the tweet and also tell how many words there are in the tweet.
def readtweet():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        tweettest = tweet.text
        print tweettest
        tweettest = tweettest.split()
        amountwords = len(tweettest)
        print "word count:",amountwords
maketweet()
