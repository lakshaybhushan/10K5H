from flask import Flask, request, jsonify
import config
import tweepy
from ai import genText, genImage, getImagePrompt

app = Flask(__name__)

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

@app.route('/tweet', methods=['POST'])
def generate_and_tweet():
    try:
        generatedText = genText()
        imagePrompt = getImagePrompt(generatedText)
        generatedImage, generatedImageName = genImage(imagePrompt)

        api.verify_credentials()
        print("Authentication ✅")


        image_id = api.media_upload(filename=f"images/{generatedImageName}").media_id_string
        client.create_tweet(text=generatedText, media_ids=[image_id])

        response = {
            'image_id': image_id,
            'generatedText': generatedText,
            'imagePrompt': imagePrompt,
            'message': "Tweet posted successfully! ✅"
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
