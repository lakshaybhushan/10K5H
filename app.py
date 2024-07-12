import config
import tweepy
from ai import getResponse

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

client = tweepy.Client(
    config.BEARER_TOKEN,
    config.CONSUMER_KEY,
    config.CONSUMER_SECRET,
    config.ACCESS_TOKEN,
    config.ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)
postText = getResponse()

try:
    api.verify_credentials()
    print("Authentication ✅")
    # client.create_tweet(text=postText)
    print("Tweet posted successfully! ✅" + postText)
except Exception as e:
    print(e)
