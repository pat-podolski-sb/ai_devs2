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

  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  ) 
  
  openResponseWithJSONFnDefinition = client.chat.completions.create(
    messages=[
      {"role": "system", "content":"Nie zwracaj odpowiedzi na pytanie tylko zwróć Imię i Nazwisko osoby z pytania. Zwracaj pełne Imię bez zdrobnień. Na przykład Krysia = Krystyna czy Tomek = Tomasz. Nie zwracaj zadnych znaków interpunkcyjnych."},
      # {"role": "system", "content":"To answer the question use data set in given link: " +  taskObject.get('data') + ". Please answer in Polish language only in one word. Favorite color take from 'ulubiony_kolor' properties, favourite food and place of residence take from 'o_mnie' property. Name ('imie') and lastname ('nazwisko') need to be exact match from question and in data set."},
      {"role": "user", "content": taskObject.get('question')},
    ],
    model="gpt-3.5-turbo",
    max_tokens=2200,
    temperature=1
  )
  pprint('Persons Name and Last Name from question FROM call_openai_api METHOD:')
  answerToQuestionBasedOnArticle = openResponseWithJSONFnDefinition.choices[0].message.content
  print(answerToQuestionBasedOnArticle)

  userObject = answerToQuestionBasedOnArticle.split(' ')
  userName = userObject[0]
  userLastName = userObject[1]
  pprint('User Name:')
  pprint(userName)
  pprint('User Last Name:')
  pprint(userLastName)
  personsDB = requests.get('https://tasks.aidevs.pl/data/people.json')
  
  
  # print(personsDB.json())
  userObject = {}
  
  for person in personsDB.json():
    if person.get('imie') == userName and person.get('nazwisko') == userLastName:
      pprint(person.get('imie') + ' ' + person.get('nazwisko'))
      userObject = person
      break
  
  pprint('User Object:')
  pprint(userObject)
  # Submit result to the API
  
  # answerObject = send_answer_to_api(tokenObject.get('token'), answerToQuestionBasedOnArticle)
  # pprint('ANSWER FROM send_answer_to_api METHOD:')
  # pprint(answerObject)