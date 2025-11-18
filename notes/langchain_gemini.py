import os

os.environ["GOOGLE_API_KEY"] = 'AIzaSyB6eE6D4567nbSiOj9m9b5nUvfKjZ0v22A'
print(os.environ["GOOGLE_API_KEY"])
print(os.environ.values())


from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

print('llm', llm)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

messages = [
    (
        "system",
        "Please answer the question.",
    ),
    ("human", "which country has more population, canada, us or uk"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

messages = [
    (
        "system",
        "Please answer the question.",
    ),
    ("human", "write python code to loop from 1 to 10"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)