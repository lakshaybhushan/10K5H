import config
import tweepy
from ai import genText, genImage, getImagePrompt

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

generatedText = genText()
imagePrompt = getImagePrompt(generatedText)
generatedImage, generatedImageName = genImage(imagePrompt)

try:
    api.verify_credentials()
    print("Authentication ✅")

    image_id = api.media_upload(filename=f"images/{generatedImageName}").media_id_string
    client.create_tweet(text=generatedText, media_ids=[image_id])
    
    print(image_id)
    print(generatedText)
    print(imagePrompt)
    print("Tweet posted successfully! ✅ \n")

except Exception as e:
    print(e)
