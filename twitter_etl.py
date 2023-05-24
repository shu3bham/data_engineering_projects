import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import re


#function to remove url



#twitter authetication
Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAJAYigEAAAAAN1Fuk%2B2EsNSaqcrBz3UGGP8j%2BFs%3DGVczWyYOuBEQH0JldmeCzxXMh4jvusPmhJTUZj24YOMAD9EZGE'
auth = tweepy.OAuth2BearerHandler(Bearer_Token)

#creating an api object
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@FoxNews',count = 2000, include_rts = False, tweet_mode = 'extended')
tweet_list=[]



for tweet in tweets:
    text =tweet._json['full_text']

    refined_tweet = {
        "user":tweet.user.screen_name,
        "text": text,
        "favorite_count" : tweet.favorite_count,
        "retweet_count" : tweet.retweet_count,
        "created_at" : tweet.created_at

    }

    tweet_list.append(refined_tweet)



#creating dataFrame
df = pd.DataFrame(tweet_list)
df.to_csv("fox_news_tweet_data.csv")






