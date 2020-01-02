import tweepy
import twitter_credentials
import time 
from datetime import datetime
import telegram

ellie = telegram.Bot(token=twitter_credentials.TELEGA_TOKEN)

keywords = ['china']

sentList = []

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.me()

def main():

    posts = api.user_timeline('realDonaldTrump', count=100)

    for post in posts:
        status = post._json['text']

        if any (keyword in status.lower() for keyword in keywords):
            if post._json['id'] not in sentList:
                sentList.append(post._json['id'])
                link = 'https://twitter.com/' + post._json['user']['screen_name'] + '/status/' + str(post._json['id'])
                message = '\nStatus:\n' + status + '\nLink:\n' + link
                print(message)
                print(sentList)
                ellie.sendMessage('561191777', message)

while True:
    try:
        main()
        print('Checking')
    except:
        print('Breaking')
        break