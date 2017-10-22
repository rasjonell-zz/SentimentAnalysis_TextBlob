import tweepy           
import pandas as pd     
import numpy as np      

from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from credentials import *
from textblob import TextBlob
import re


def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


extractor = twitter_setup()

tweets = extractor.search(q="#SampleHashtag", count = 200) # CHANGE THE HASHTAG, IN ORDER NOT TO GET DIVISION BY ZERO ERROR!

print("Number of tweets extracted: {}.\n".format(len(tweets)))


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analize_sentiment(tweet):
    # Simple implementation of the sgn(x) function to make the analysis more comprenesive. 
    
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])    
data['ID'] = np.array([tweet.id for tweet in tweets])
data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
print("Percentage of negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))


display(data.head(20))

