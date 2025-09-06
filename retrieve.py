from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

# from llm import *

embeddings = OllamaEmbeddings(model="llama3.2:1b")

url ="https://9731d9ce-cbf4-4495-b840-9b220a8cd953.us-west-1-0.aws.cloud.qdrant.io:6333"
api_key =os.getenv("QDRANT_API_KEY")

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=url,
    api_key=api_key,
    collection_name="Motor_Act",
)

response =  qdrant.similarity_search(
    query=question,
    k=5)

print(response)
# for score in response:
#     print(  score)

prompt = f"""

Question: {question},
context: {response}
Only return the summary based on the provided content.
"""

# print(completion_llm(prompt))