import config
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create an API object
api = tweepy.API(auth)

# Create an Client object
client = tweepy.Client(
    config.BEARER_TOKEN,
    config.CONSUMER_KEY,
    config.CONSUMER_SECRET,
    config.ACCESS_TOKEN,
    config.ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

postText = "Hello, X!"

try:
    api.verify_credentials()
    print("Authentication OK")
    # client.create_tweet(text=postText)
    print("Tweet posted successfully!")
except Exception as e:
    print(e)
