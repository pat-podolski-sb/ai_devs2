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

  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  ) 
  
  openaiResponseWithQuestionCategory = client.chat.completions.create(
      messages=[
        {"role": "system", "content": 'I Decide whether the task should be added to the ToDo list or to the calendar (if time is provided) '
        'and return the corresponding JSON. '
        'I always use YYYY-MM-DD format for dates \n'
        'If task has provided duration, and not date I classify as ToDo\n'
        'For example:\n'
        'Q: Jutro mam spotkanie z Marianem\n'
        'A: {{"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2024-04-10"}}\n'
        'Q: Przypomnij mi, że mam kupić mleko\n'
        'A: {{"tool":"ToDo","desc":"Kup mleko" }}\n'
        'Context:###:\n'
        'Today is: 2024-04-10\n'},
        {"role": "user", "content": taskObject.get('question')},
      ],
      model="gpt-3.5-turbo",
      max_tokens=2200,
      temperature=1
    )
  pprint('Question category FROM call_openai_api METHOD:')
  questionCategory = openaiResponseWithQuestionCategory.choices[0].message.content
  answerToJSON = json.loads(questionCategory)

  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), answerToJSON)
    
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)