import requests
import os
# from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_token_from_api(task_name):
  api_url = 'https://tasks.aidevs.pl/token/' + task_name
  body = {'apikey': os.getenv('AI_DEVS_2_API_KEY')}

  getTokenEndpointResponse = requests.post(
    api_url, json=body, headers={'Content-Type': 'application/json'}
  )  

  getTokenEndpointResponse.raise_for_status()
  return getTokenEndpointResponse.json()


def get_task_from_api(token):
  api_url = 'https://tasks.aidevs.pl/task/' + token

  getTaskEndpointResponse = requests.get(
    api_url, headers={'Content-Type': 'application/json'}
  )

  getTaskEndpointResponse.raise_for_status()
  return getTaskEndpointResponse.json()

def send_answer_to_api(token, answer):
  api_url = 'https://tasks.aidevs.pl/answer/' + token
  body = {'answer': answer}

  postAnswerEndpointResponse = requests.post(
    api_url, json=body, 
    headers={'Content-Type': 'application/json'}
  )

  # postAnswerEndpointResponse.raise_for_status()
  return postAnswerEndpointResponse.json()

def call_openai_api(systemContent = '', userContent = ''):
  api_url = 'https://api.openai.com/v1/chat/completions'
  bearerAuth = 'Bearer ' + os.getenv('OPENAI_API_KEY')

  body = {
     "messages": [
       { "role": "system", "content": systemContent },
       { "role": "user", "content": userContent}
      ],
     "model": "gpt-3.5-turbo",
      "max_tokens": 2200,
      "temperature": 1,
      # "top_p": 1,
      # "frequency_penalty": 0,
      # "presence_penalty": 0,
      # "stop": "\n",
      # "logprobs": 0,
      # "echo": "true",
      # "user": "user",
      # "content": "Hello!",
      # "role": "user",
      # "type": "message",
      # "id": "user_0",
      # "timestamp": 1643092800,
      # "is_typing": "false",
      # "is_action": "false",
  }
  setHeaders = {'Content-Type': 'application/json', 'Authorization': bearerAuth}
  print('setHeaders:', setHeaders)
  getResponseFromOpenai = requests.post(
    api_url, json=body, headers=setHeaders #, auth=bearerAuth
  )
  
  # client = OpenAI(
  #   # This is the default and can be omitted
  #   api_key=os.getenv('OPENAI_API_KEY')
  # )

  # chat_completion = client.chat.completions.create(
  #   messages=[
  #     { "role": "system", "content": aaa },
  #     { "role": "user", "content": userContent}
  #   ],
  #   model="gpt-3.5-turbo",
  #   max_tokens=2200,
  #   temperature=1
  # )
  
  # chat_completion.raise_for_status()
  # print(chat_completion.choices[0].message.content[1])
  
  
  return getResponseFromOpenai.json()