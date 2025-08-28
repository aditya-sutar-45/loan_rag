from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from documents import load_documents


if __name__ == "__main__":
    load_dotenv()
    print("getting documents...")
    pdf_path = "./data/*.pdf"
    docs = load_documents(pdf_path=pdf_path)
    print(f"retreived {len(docs)} documents...")


    # embeddings = OllamaEmbeddings(model="nomic-embed-text:v1.5")
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    print("Ingesting...")
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local("./data/db")
    print("Saved to local file...")
