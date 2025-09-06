from langchain_community.document_loaders import PyPDFLoader
import os

data_folder = "./data"
pdf_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.lower().endswith(".pdf")]
print(pdf_files)

# loaders = [PyPDFLoader(pdf_file) for pdf_file in pdf_files]