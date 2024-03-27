from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_inprompt_05(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('input FROM get_task_from_api METHOD:')
  pprint(taskObject.get('input'))
  pprint('question FROM get_task_from_api METHOD:')
  pprint(taskObject.get('question'))
  
  retrieveNameFromString = re.findall(r'\b[A-Z]\w*', taskObject.get('question'))[0]
  pprint('Retrieve name from question:')
  pprint(retrieveNameFromString)
  
  filteredQuestion = list(filter(lambda x: x.find(retrieveNameFromString) != -1, taskObject.get('input')))
  pprint('Filtered question:')
  pprint(filteredQuestion)
  
  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), filteredQuestion[0])
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)