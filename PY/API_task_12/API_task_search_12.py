from pprint import pprint
import json
import os
import requests
import re
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient, models
from utils import get_token_from_api, get_task_from_api, send_answer_to_api


# C03L04
def api_test_search_12(taskName):
  # Get TOKEN
  tokenObject = get_token_from_api(taskName)
  pprint('TOKEN FROM get_token_from_api METHOD:')
  pprint(tokenObject.get('token'))

  # Get TASK
  taskObject = get_task_from_api(tokenObject.get('token'))
  pprint('Object FROM get_task_from_api METHOD:')
  print(taskObject)

  qdrantClient = QdrantClient(url=os.getenv('QDRANT_URL'))
  embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1536)

  # Convert the question to an embedding
  questionEmbedding = embeddings.embed_query(taskObject.get('question'))
  
  # Make an API call to a vector DB Qdrant for closest hit
  closestHit = qdrantClient.search(
    collection_name='ai_devs', 
    query_vector=questionEmbedding, 
    limit=1
  )
  
  pprint('Closest hits:')
  pprint(closestHit)
    
  answerObject = send_answer_to_api(tokenObject.get('token'), closestHit[0].payload.get('url'))
  pprint('ANSWER FROM send_answer_to_api METHOD:')
  pprint(answerObject)