from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

# C05L01
def api_test_meme_19(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

    
  # client = OpenAI(
  #   api_key=os.getenv('OPENAI_API_KEY')
  # ) 
  
  # openaiResponseWithQuestionCategory = client.chat.completions.create(
  #     messages=[
  #       {"role": "user", "content": [
  #         {"type": "text", "text": taskObject.get('msg')},
  #         {
  #           "type": "image_url",
  #           "image_url": {
  #             "url": taskObject.get('url'),
  #           },
  #         },
  #       ]},
  #     ],
  #     model="gpt-4-turbo",
  #     max_tokens=2200,
  #     temperature=1
  #   )
  # pprint('Question category FROM call_openai_api METHOD:')
  # questionCategory = openaiResponseWithQuestionCategory.choices[0].message.content
  # print(questionCategory)
    
  # # Submit result to the API
  # tokenObject = get_token_from_api(taskName)
  # answerObject = send_answer_to_api(tokenObject.get('token'), questionCategory)
  # pprint('ANSWER FROM send_answer_to_api METHOD:')
  # pprint(answerObject)