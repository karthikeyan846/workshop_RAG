from langchain_community.document_loaders import PyPDFLoader
# import os

data_folder = "./data/eng.pdf"

loader = PyPDFLoader(data_folder)
data = loader.load_and_split()

# print(docs[0])

# from qdrant_client import QdrantClient

# qdrant_client = QdrantClient(
#     url="https://9731d9ce-cbf4-4495-b840-9b220a8cd953.us-west-1-0.aws.cloud.qdrant.io:6333", 
#     api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.QFclDuzPWVT9SlZ3V1nANM2FfeCEm-Vn9aMzCdgdrfQ",
# )

# print(qdrant_client.get_collections())
