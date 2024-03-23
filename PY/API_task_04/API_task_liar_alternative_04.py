from pprint import pprint
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_task_alternative_04(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('TASK FROM get_task_from_api METHOD:')
  pprint(taskObject)

  # Send POST to /task/ endpoint to get the answer for the question
  mainQuestion = 'What is the capital of Argentina?'
  answerInLowerCase = 'buenos aires'
  
  taskPostResponse = requests.post(
    'https://tasks.aidevs.pl/task/' + tokenObject.get('token'), data={'question': mainQuestion}) 
  taskPostResponse.raise_for_status()
  pprint('TASK POST RESPONSE:')
  taskPostResponseAnswer = taskPostResponse.json().get('answer')
  pprint(taskPostResponseAnswer)
  
  doesAnswerMatchQuestion = 'NO'
  if re.search(answerInLowerCase, taskPostResponseAnswer.lower()):
    doesAnswerMatchQuestion = 'YES'


  # Submit result to the API
  pprint('Is the answer correct for the question? => '+doesAnswerMatchQuestion)
  answerObject = send_answer_to_api(tokenObject.get('token'), doesAnswerMatchQuestion)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)