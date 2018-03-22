import random
import json
import tweepy
from tweepy import OAuthHandler
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
callbackurl = 'https://twitter.com/settings/devices?success=true'
consumer_key = ''
consumer_secret = ''
access_token = '8h'
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,callbackurl)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
#this function will make a random tweet made up of one of these letters.note:Sometimes it picks the same letter.
def maketweet():
    randomletters = random.choice(['amir','baka','corner','destiny','ellen','finish','getitdone','h','i','t','v','W','X','w','x','z','y','B','U','Y'])
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
