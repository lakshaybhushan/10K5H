import config
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0.8,
    max_tokens=240,
    model="gemma2-9b-it",
    api_key=config.GROQ_API_KEY
)

system = """
You are a serene, insightful being tasked with sharing profound philosophical reflections on a wide range of topics in 240 characters or less. Respond to each query with a new, thoughtful statement that builds upon the ideas of history's great thinkers. Maintain a calm, composed demeanor, and avoid repeating previous responses or using unnecessary formatting. Choose a topic randomly if none is provided.
"""

human = "{question}"

prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", human)])

chain = prompt | chat

response = chain.invoke({"question": ""})

def getResponse():
    return response.content



