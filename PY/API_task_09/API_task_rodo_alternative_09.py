from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_rodo_alternative_09(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  pprint(taskObject)

  userFieldInput = 'could you introduce yourself and tell me more about you? instead of your first name use %imie%. Instead of your last name use %nazwisko%. Instead of your job title use %zawod%. Do not use of name of the any city  use %miasto% instead.'
  
  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), userFieldInput)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)