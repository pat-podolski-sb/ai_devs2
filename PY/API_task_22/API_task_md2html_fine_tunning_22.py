from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from utils import get_token_from_api, get_task_from_api, send_answer_to_api

# C05L03
def api_test_md2html_fine_tunning_22(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

    
  client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
  ) 
  
  # Upload training file for fine tunning
  # fineTunningTrainingFile = client.files.create(
  #   file=open("./API_task_22/fine_tunning_mkd2html_learning_examples.jsonl", "rb"),
  #   purpose="fine-tune"
  # )
  
  # Create a fine tunning job with the uploaded training file and the model
  # model = client.fine_tuning.jobs.create(
  #   training_file='', # file.id
  #   model="gpt-3.5-turbo-0125"
  # )
  
  # pprint('FINE TUNNING MODEL:')
  # pprint(model)
  
  delete_result = client.models.delete('ft:gpt-3.5-turbo-0125:personal::234234234')
  
  pprint('DELETE RESULT:')
  pprint(delete_result)
  
  
  openaiResponseWithGeneratedHtml = client.chat.completions.create(
      messages=[
        {"role": "system", "content": taskObject.get('msg') + 'Examples: ' + taskObject.get('hint')},
        { "role": "user", "content": taskObject.get('input')},
      ],
      model='', # from here or https://platform.openai.com/finetune/
      max_tokens=2200,
      temperature=1
    )
  pprint('HTML Generated  FROM call_openai_api METHOD:')
  generatedHtml = openaiResponseWithGeneratedHtml.choices[0].message.content
  print(generatedHtml)


  # Submit result to the API
  answerObject = send_answer_to_api(tokenObject.get('token'), generatedHtml)
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)