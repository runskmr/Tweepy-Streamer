import tweepy


consumer_key = "q6kbMsPp6Zd4xxi7hRh1qU3Ah"
consumer_secret = "5tI8HdqYGxiHRAVvTDj3iWIidNvc9VNg6ttSS8ECQqFXiZvrvV"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFovdgEAAAAAu%2B05u%2BDVThFnkqU9xXWMwdVtkec%3DR14uqAx36qE1qzALY2AN0ewX7kLJJVGeG3izEWVZ5mabwOa28T"
access_token = "4423275673-DSeWCKbQ91LTIjLMFzq458RYSvJaCRtRHvuJP8O"
access_token_secret = "yiwRBEPVAQR5eDJpXXpWCCx7FOLiFa6DFqSVhk9enVjG2"

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

