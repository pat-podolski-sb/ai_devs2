from qdrant_client import QdrantClient, models
from langchain_openai import OpenAIEmbeddings
import requests
from pprint import pprint
import os
from dotenv import load_dotenv, find_dotenv

COLLECTION_NAME = 'ai_devs'
load_dotenv(find_dotenv())

qdrantClient = QdrantClient(url=os.getenv('QDRANT_URL'))
# https://github.com/qdrant/qdrant-client
# https://github.com/i-am-alice/2nd-devs/blob/main/27_qdrant/27.ts

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1024)
text = "This is a test document."
query_result = embeddings.embed_query(text)

# pprint(query_result)
pprint('works')


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

    # Get list of collections
    # listOfQdrantCollections = qdrantClient.get_collections()

    # pprint(listOfQdrantCollections)

    # collections_list = []
    # for collection in listOfQdrantCollections:
    #     print(collection)
    #     for collectionObject in list(collection[1]):
    #         collections_list.append(collectionObject.name)
    #         print(collectionObject.name)

    # pprint(collections_list)
    # pprint(collections_list.count(COLLECTION_NAME))

    # if collections_list.count(COLLECTION_NAME) == 1:
    #     pprint('Collection created successfully')
    # else:
    #     pprint('Collection not created')
       
       

# Delete collection:
# qdrantClient.delete_collection(collection_name=COLLECTION_NAME)