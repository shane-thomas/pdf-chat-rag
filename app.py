from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS

pdfs_directory = 'pdfs/'
embeddings = OllamaEmbeddings(model = "nomic-embed-text")

model = OllamaLLM(model = "gemma3")
template = """
You are an assistant that answers questions. Using the following retrieved information, answer the user question. If you don't know the answer, say that you don't know. Use up to three sentences, keeping the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

def upload_pdf(file):
    
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def create_vector_store(file_path):
    print("\nLoading PDF\n")
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print("\nLoaded PDF, now splitting text into chunks\n")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300, add_start_index=True)
    print("\nSplit text into chunks. Now creating Vector Store\n")
    chunked_docs = text_splitter.split_documents(documents)
    texts = [doc.page_content for doc in chunked_docs]
    db = FAISS.from_texts(texts, embeddings)
    print("Created Vector Store successfully.")
    return db


def retrieve_docs(db, query, k=4):  
    print(db.similarity_search(query))
    return db.similarity_search(query, k)


def question_pdf(question, documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})