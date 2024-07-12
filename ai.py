import config
from groq import Groq

client = Groq(api_key=config.GROQ_API_KEY)


def getResponse():
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "assistant", "content": "You are twitter bot, you have to give a new unique philosophical from past saying/wording in less than 40 words evertime user say 'tell me' in plain text. NO REPEATS! NO MARKDOWN! NO EMOJIS! NO LINKS!"},

            {"role": "user", "content": "tell me"},
        ],
        model="gemma2-9b-it",
        max_tokens=80,
        temperature=0.8,
    )

    return chat_completion.choices[0].message.content
