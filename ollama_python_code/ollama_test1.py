import ollama
import streamlit

print('models: ', ollama.list())
# print('models: ', ollama.ps())
# print('models: ', ollama.show('deepseek-r1:1.5b'))
print(streamlit.__version__)

from ollama import chat
from ollama import ChatResponse

while True:
    prompt = input('please ask: ')
    response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
