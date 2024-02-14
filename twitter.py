import tweepy
from datetime import datetime, timedelta



api_key = 
api_secret_key = 
access_token = 
access_token_secret =
username = 

def authen(api_key, api_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def collect(api,user,since_date,until_date):
    tweets=[]
    for i in tweepy.Cursor(api.user_timeline,screen_name=user,since=since_date,until=until_date).items():
        tweets.append(i)
    return tweets

def collect_previous_month_tweets(api_key, api_secret_key, access_token, access_token_secret, username):
    api = authen(api_key, api_secret_key, access_token, access_token_secret)
    today = datetime.now()
    last_month = today - timedelta(days=30)
    tweets = collect(api, username, last_month, today)
    return tweets

tweets = collect_previous_month_tweets(api_key, api_secret_key, access_token, access_token_secret, username)
for tweet in tweets:
    print(tweet.text)