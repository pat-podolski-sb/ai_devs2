from pprint import pprint
import json
import os
from openai import OpenAI
from ai_devs2_utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_task_03(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('TASK FROM get_task_from_api METHOD:')
  pprint(taskObject)


  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  )
  
  arrayOfAnswers = []
  
  for item in taskObject.get('input'):
    itemResponse = client.moderations.create(
      input=item,
      model='text-moderation-latest'
    )
    isFlagged = itemResponse.results[0].flagged
    pprint('ANSWER FROM call_openai_api METHOD:')
    pprint(isFlagged)
    arrayOfAnswers.append(int(isFlagged))

  pprint('ANSWER FROM call_openai_api METHOD:')
  pprint(arrayOfAnswers)

  # Send ANSWER
  answerObject = send_answer_to_api(tokenObject.get('token'), arrayOfAnswers)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)