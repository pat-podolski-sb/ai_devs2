from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

# C04L02
def api_test_tools_15(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

    
  # TODO: Implement the logic of the task

  # client = OpenAI(
  #   api_key=os.getenv('OPENAI_API_KEY')
  # ) 
  
  # openaiResponseWithQuestionCategory = client.chat.completions.create(
  #     messages=[
  #       {"role": "system", "content": "Having 3 categories: population, currency, general. What is the category of the question? If answer is population please add name of a country after name of category. If answer is currency please add name of a currency after name of category. If answer is general don't add anything else. Example: population Poland, currency EUR, general."},
  #       {"role": "user", "content": taskObject.get('question')},
  #     ],
  #     model="gpt-3.5-turbo",
  #     max_tokens=2200,
  #     temperature=1
  #   )
  # pprint('Question category FROM call_openai_api METHOD:')
  # questionCategory = openaiResponseWithQuestionCategory.choices[0].message.content
  # print(questionCategory)
    
  # Submit result to the API
  tokenObject = get_token_from_api(taskName)
  answerObject = send_answer_to_api(tokenObject.get('token'), 'responseForQuestion')
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)