from pprint import pprint
import json
import os
import requests
from openai import OpenAI
from ai_devs2_utils import get_token_from_api, get_task_from_api, send_answer_to_api

def api_test_task_04(taskName):
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
  
  # Create a random question about geography
  openApiQuestionResponse = client.chat.completions.create(
    messages=[
      {"role": "user", "content": 'Please generate me one random question about a geography.'},
    ],
    model="gpt-3.5-turbo",
    max_tokens=2200,
    temperature=1
  )
  pprint('QUESTION FROM call_openai_api METHOD:')
  randomQuestionAboutGeography = openApiQuestionResponse.choices[0].message.content
  pprint(randomQuestionAboutGeography)

  # Send POST to /task/ endpoint to get the answer for the question
  taskPostResponse = requests.post(
    'https://tasks.aidevs.pl/task/' + tokenObject.get('token'), data={'question': randomQuestionAboutGeography}) 
  taskPostResponse.raise_for_status()
  pprint('TASK POST RESPONSE:')
  taskPostResponseAnswer = taskPostResponse.json().get('answer')
  pprint(taskPostResponseAnswer)
  
  # Verify the answer to the question
  openApiAnswerVsQuestionResponse = client.chat.completions.create(
    messages=[
      {"role": "user", "content": 'Please tell me if the answer to the provided question is correct or not. Respond YES/NO. '+randomQuestionAboutGeography+' '+taskPostResponseAnswer}
    ],
    model="gpt-3.5-turbo",
    max_tokens=2200,
    temperature=1
  )
  
  pprint('ANSWER FROM call_openai_api METHOD:')
  isAnswerCorrectForGivenQuestion = openApiAnswerVsQuestionResponse.choices[0].message.content
  pprint(openApiAnswerVsQuestionResponse.choices[0].message.content)

  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), isAnswerCorrectForGivenQuestion)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)