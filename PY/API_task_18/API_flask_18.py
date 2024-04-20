from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# --------------------------------------------------------------
# Create flask app
# --------------------------------------------------------------
from flask import Flask, request
app = Flask(__name__)

# --------------------------------------------------------------
# Define available methods and route
# --------------------------------------------------------------

chat = ChatOpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
  model="gpt-4",
)

conversation = ConversationChain(
    llm=chat, verbose=True, memory=ConversationBufferMemory()
)

@app.route('/ownapipro', methods=['POST'])
def api_test_ownapi_18():
  
  if request.method == 'POST':
    
    pprint('REQUEST:')
    pprint(request.json)
    
    pprint('REQUEST TASK NAME:')
    pprint(request.json.get('question'))
    

    # client = OpenAI(
    #   api_key=os.getenv('OPENAI_API_KEY')
    # ) 
    
    # openResponseToAskedQuestion = client.chat.completions.create(
    #   messages=[
    #     {"role": "system", "content": "Answer given question."},
    #     {"role": "user", "content": request.json.get('question')},
    #   ],
    #   model="gpt-3.5-turbo",
    #   max_tokens=2200,
    #   temperature=1
    # )
    openResponseToAskedQuestion = conversation.predict(input= request.json.get('question'))
    pprint('OpenAI REPSPONSE:')
    pprint(openResponseToAskedQuestion)
    
    answer_to_the_user = {'reply': openResponseToAskedQuestion}
  return answer_to_the_user

@app.route('/ownapi', methods=['GET'])
def api_test_ownapi_18_get():
  
  return 'GET method not allowed', 405

if __name__ == '__main__':
  app.run(port=8080, debug=True)