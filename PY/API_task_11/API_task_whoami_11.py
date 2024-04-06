from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_whoami_11(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # # Get TASK
  # taskObject = get_task_from_api(tokenObject.get('token'))
  # pprint('Object FROM get_task_from_api METHOD:')
  # print(taskObject)

  # TODO: Implement the logic of the task

  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  ) 
  
  list_of_hints = []
  is_model_certain = "NO"
  
  while is_model_certain == "NO":
      # Get TOKEN
    tokenObject = get_token_from_api(taskName)
    pprint('TOKEN FROM get_token_from_api METHOD:')
    pprint(tokenObject.get('token'))
    
      # Get TASK
    taskObject = get_task_from_api(tokenObject.get('token'))
    pprint('Object FROM get_task_from_api METHOD:')
    print(taskObject)
    
    list_of_hints.append(taskObject.get('hint'))
    openResponseWithJSONFnDefinition = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "Are you certain about what famous person is that information? Return YES/NO." },
        {"role": "user", "content": json.dumps(list_of_hints)},
      ],
      model="gpt-3.5-turbo",
      max_tokens=2200,
      temperature=1
    )
    pprint('Function definition FROM call_openai_api METHOD:')
    answerToQuestionBasedOnArticle = openResponseWithJSONFnDefinition.choices[0].message.content
    print(answerToQuestionBasedOnArticle)
    is_model_certain = answerToQuestionBasedOnArticle
  
  openResponseWithJSONFnDefinition = client.chat.completions.create(
    messages=[
      {"role": "system", "content": "I'm famous person. Who am I based on given hints. Please Return only name and lastname. " },
      {"role": "user", "content": json.dumps(list_of_hints)},
    ],
    model="gpt-3.5-turbo",
    max_tokens=2200,
    temperature=1
  )
  pprint('Function definition FROM call_openai_api METHOD:')
  answerToQuestionBasedOnArticle = openResponseWithJSONFnDefinition.choices[0].message.content
  print(answerToQuestionBasedOnArticle)

  

  # Submit result to the API
  tokenObject = get_token_from_api(taskName)
  answerObject = send_answer_to_api(tokenObject.get('token'), answerToQuestionBasedOnArticle)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)