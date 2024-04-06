from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct
from langchain_openai import OpenAIEmbeddings
import requests
from pprint import pprint
import json
import os
import uuid
from dotenv import load_dotenv, find_dotenv

COLLECTION_NAME = 'ai_devs'
load_dotenv(find_dotenv())

qdrantClient = QdrantClient(url=os.getenv('QDRANT_URL'))
# https://github.com/qdrant/qdrant-client
# https://github.com/i-am-alice/2nd-devs/blob/main/27_qdrant/27.ts

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1536)

qdrantClient.delete_collection(collection_name="ai_devs")
# Get list of collections
listOfQdrantCollections = qdrantClient.get_collections()

pprint(listOfQdrantCollections)

collections_list = []
for collection in listOfQdrantCollections:
    print(collection)
    for collectionObject in list(collection[1]):
        collections_list.append(collectionObject.name)
        print(collectionObject.name)


pprint(collections_list)
pprint(collections_list.count(COLLECTION_NAME))

if collections_list.count(COLLECTION_NAME) == 0:
    # Create a collection
    qdrantClient.create_collection(
      collection_name=COLLECTION_NAME , 
      vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE,on_disk=True))

listOfItems = requests.get('https://unknow.news/archiwum_aidevs.json').json()

pprint(len(listOfItems))

for item in listOfItems:
    item['metadata'] = {
      'source': COLLECTION_NAME,
      'content': item['title'],
      'uuid': uuid.uuid4(),
      'url': item['url']
    }
    
pprint(listOfItems[0])

points = []
for item in listOfItems:
  embedding = embeddings.embed_query(item['title'])
  points.append({
    'id': str(item['metadata']['uuid']),
    'vector': embedding,
    'metadata': item['metadata']
  })

pprint(points[0]['metadata'])

qdrantClient.upsert(
  collection_name=COLLECTION_NAME, 
  points=[PointStruct(
    id=point['id'], 
    vector=point['vector'], 
    payload=point['metadata']
  ) for id, point in enumerate(points)])

# Delete collection:
# qdrantClient.delete_collection(collection_name="{COLLECTION_NAME}")