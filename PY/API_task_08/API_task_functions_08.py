from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_functions_08(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

  # Submit result to the API
  functionDefinition = json.load(open('./API_task_08/functionDefinition.json', encoding="utf-8"))
  
  pprint('Function definition:')
  pprint(functionDefinition)
  
  answerObject = send_answer_to_api(tokenObject.get('token'), functionDefinition)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)