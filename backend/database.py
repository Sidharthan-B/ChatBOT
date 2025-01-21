from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def setup_knowledge_base():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory="./data/chroma", embedding_function=embeddings)

def query_knowledge_base(user_query):
    vectorstore = setup_knowledge_base()
    docs = vectorstore.similarity_search(user_query, k=3)
    return "\n".join([doc.page_content for doc in docs])
