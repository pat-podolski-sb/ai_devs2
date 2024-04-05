from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = QdrantClient(url=os.getenv('QDRANT_URL'))
# https://github.com/qdrant/qdrant-client
# https://github.com/i-am-alice/2nd-devs/blob/main/27_qdrant/27.ts
print('works')