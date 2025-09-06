from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

data_folder = "./data/eng.pdf"
loader = PyPDFLoader(data_folder)
docs = loader.load_and_split()



embeddings = OllamaEmbeddings(model="llama3.2:latest")
url = "https://9731d9ce-cbf4-4495-b840-9b220a8cd953.us-west-1-0.aws.cloud.qdrant.io:6333"
api_key = os.getenv("QDRANT_API_KEY")
print(url, api_key)


qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="Motor_Act",
)

print("Uploaded to Qdrant")