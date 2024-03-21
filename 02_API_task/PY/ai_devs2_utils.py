import requests
import os
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
    api_url, json=body, headers={'Content-Type': 'application/json'}
  )

  postAnswerEndpointResponse.raise_for_status()
  return postAnswerEndpointResponse.json()