from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_whisper_07(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  pprint(taskObject)

  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  ) 
  
  # Create a random question about geography
  mp3File = requests.get('https://tasks.aidevs.pl/data/mateusz.mp3')
  with open('./API_task_07/mateusz.mp3', 'wb') as f:
    f.write(mp3File.content)
    
  openApiQuestionResponse = client.audio.transcriptions.create(
    file=open('./API_task_07/mateusz.mp3', 'rb'),
    model="whisper-1",
    response_format="text"
  )
  pprint('Number of Embeddings FROM call_openai_api METHOD:')
  pprint(openApiQuestionResponse)
  
  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), openApiQuestionResponse)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)