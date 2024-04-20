from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI


# --------------------------------------------------------------
# Create flask app
# --------------------------------------------------------------
from flask import Flask, request
app = Flask(__name__)

# --------------------------------------------------------------
# Define available methods and route
# --------------------------------------------------------------

@app.route('/ownapi', methods=['POST'])
def api_test_ownapi_17():
  
  if request.method == 'POST':
    
    pprint('REQUEST:')
    pprint(request.json)
    
    pprint('REQUEST TASK NAME:')
    pprint(request.json.get('question'))
    

    client = OpenAI(
      api_key=os.getenv('OPENAI_API_KEY')
    ) 
    
    openResponseToAskedQuestion = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "Answer given question."},
        {"role": "user", "content": request.json.get('question')},
      ],
      model="gpt-3.5-turbo",
      max_tokens=2200,
      temperature=1
    )
    
    pprint('OpenAI REPSPONSE:')
    pprint(openResponseToAskedQuestion.choices[0].message.content)
    
    answer_to_the_user = {'reply': openResponseToAskedQuestion.choices[0].message.content}
  return answer_to_the_user

@app.route('/ownapi', methods=['GET'])
def api_test_ownapi_17_get():
  
  return 'GET method not allowed', 405

if __name__ == '__main__':
  app.run(port=8080, debug=True)