from pprint import pprint
import json
import os
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api



def api_test_task_02(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))


  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('TASK FROM get_task_from_api METHOD:')
  pprint(taskObject)

  pprint(taskObject.get('msg'))
  pprint(json.dumps(taskObject.get('blog')))

  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  )
  contentContinuation = " Each paragraph is separated by comma in input. Respond in the same format the question came e.g. ['response for the first item', 'response for the next item']. Do not make line breaks in answer."
  
  openApiResponse = client.chat.completions.create(
    messages=[
      { "role": "system", "content": taskObject.get('msg') + contentContinuation },
      { "role": "user", "content": json.dumps(taskObject.get('blog'))}
    ],
    model="gpt-3.5-turbo",
    max_tokens=2200,
    temperature=1
  )

  pprint('ANSWER FROM call_openai_api METHOD:')
  contentList = json.loads(openApiResponse.choices[0].message.content)
  pprint(contentList)

  # Send ANSWER
  answerObject = send_answer_to_api(tokenObject.get('token'),contentList)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)