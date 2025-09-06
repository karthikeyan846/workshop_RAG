from langchain_community.document_loaders import PyPDFLoader
# import os

data_folder = "C:/Users/karth/OneDrive/Desktop/NLP/workshop_RAG/data/eng.pdf"

loader = PyPDFLoader(data_folder)
docs = loader.load()

# print(docs[0])


