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
  
  # client = OpenAI(
  #   api_key=os.getenv('OPENAI_API_KEY')
  # ) 
  
  # # Create a random question about geography
  # openApiQuestionResponse = client.embeddings.create(
  #   input="Hawaiian pizza",
  #   model="text-embedding-ada-002"
  # )
  # pprint('Number of Embeddings FROM call_openai_api METHOD:')
  # pprint(len(openApiQuestionResponse.data[0].embedding))
  
  # # Submit result to the API
  # answerObject = send_answer_to_api(tokenObject.get('token'), openApiQuestionResponse.data[0].embedding)
  # pprint('ANSWER FROM send_answer_to_api METHOD:')
  # pprint(answerObject)