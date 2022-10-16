import tweepy


consumer_key = ""
consumer_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.get_user(screen_name='Cristiano')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

