##1. Ingest PDF files
# 2. Extract text from PDF files and split into small chucnks
# 3. send chunks to embeddings Model
# 4. save embeddings to a vector db
# 5. perform similarity searcg on the vector db to find simalrity
# 6. retrieve the similar documents and presnet them to the User

from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/pi0.pdf"
model = "llama3.2:1b"

if doc_path:
  loader = UnstructuredPDFLoader(doc_path)
  data = loader.load()
  print("done loading")
else:
  print("Please upload a PDF")

#View first page
content = data[0].page_content
print(content[:100])

# ===========End PDF Ingestion ==========

# ===========Start Extract Text from PDF and Split into Chunks ==========

# from langchain_ollama import OllamaEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community, vectorstores import Chroma

# #Same way of doing it accross the board
# #Each chuck size will be 1200 and and overlap = 300 so we are 
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
# chunks = text_splitter.split(data)
# print("done splitting")

# ===========Add to vector database ==========

#get nomic embeddings from ollama website