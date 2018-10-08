import tweepy 
from textblob import TextBlob

consumer_key = '9Ld9t9g9gZxKCOnLMIVPlsVUB'
consumer_secret = 'zXKFx9KIfTDpVXcVtE6I5HfGkcIaAKF7fryXiYvXg4LKkaGfyI'

access_token = '1027940289309286400-s4uhWJQ4Syol3KYDYzPejXR2QUPJiV'
access_token_secret = 'vqgUaJFTj6syYbnTLrlwfAwRnV3wemjAYmp1Yj7R6n1kL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets: 
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")





