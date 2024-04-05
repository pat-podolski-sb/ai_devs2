from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

# C03L05
def api_test_people_13(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

  # TODO: Implement the logic of the task

  # client = OpenAI(
  #   api_key=os.getenv('OPENAI_API_KEY')
  # ) 
  
  # openResponseWithJSONFnDefinition = client.chat.completions.create(
  #   messages=[
  #     {"role": "system", "content": taskObject.get('msg') + ". Article: " +  taskObject.get('input')},
  #     {"role": "user", "content": taskObject.get('question')},
  #   ],
  #   model="gpt-3.5-turbo",
  #   max_tokens=2200,
  #   temperature=1
  # )
  # pprint('Function definition FROM call_openai_api METHOD:')
  # answerToQuestionBasedOnArticle = openResponseWithJSONFnDefinition.choices[0].message.content
  # print(answerToQuestionBasedOnArticle)

  # # Submit result to the API
  
  # answerObject = send_answer_to_api(tokenObject.get('token'), answerToQuestionBasedOnArticle)
  # pprint('ANSWER FROM send_answer_to_api METHOD:')
  # pprint(answerObject)