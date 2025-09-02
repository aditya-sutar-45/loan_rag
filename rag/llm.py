from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

chat_history = []
rag_chain = None

def init_rag(db_path="./data/db"):
    """Initialize the RAG system once at the beginning."""
    global rag_chain
    
    # llm = ChatOllama(model="gemma3", temperature=0)
    # embeddings = OllamaEmbeddings(model="nomic-embed-text:v1.5")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    
    store = FAISS.load_local(
        db_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
    
    # Setup prompts and chains (same as above)
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm, store.as_retriever(), contextualize_q_prompt
    )

    qa_system_prompt = (
    "You are a knowledgeable mortgage and real estate assistant. "
    "Use the retrieved context to provide accurate answers about "
    "closing costs, loan terms, and mortgage documents. "
    "Always cite specific amounts when available.\n\n"

    "Output rules (strict):\n"
    "-  Do NOT include ```html or any code fences.\n"
    "- Only return HTML snippets, no <html>, <head>, or <body> tags.\n"
    "- Use <h2> for all section headings.\n"
    "- Use <p> for explanatory text and paragraphs.\n"
    "- Use <ul> and <li> for bullet point lists.\n"
    "- Use <table>, <tr>, <th>, and <td> for tabular data (must be valid HTML).\n"
    "- Do NOT include markdown, plain text, or comments.\n"
    "- Do NOT explain formatting — only return the final HTML content.\n\n"

    "The output must be clean, professional, and safe to embed directly inside a React component."
    "\n\nContext:\n{context}"
    )
    
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

def invoke_llm(question):
    global chat_history, rag_chain
    
    if rag_chain is None:
        raise ValueError("RAG system not initialized. Call initialize_rag_system() first.")
    
    # Get response
    response = rag_chain.invoke({
        "input": question,
        "chat_history": chat_history
    })
    
    # Update history
    chat_history.extend([
        HumanMessage(content=question),
        AIMessage(content=response["answer"])   
    ])

    safe_response = {
        "question": question,
        "context": [doc.page_content for doc in response.get("context", [])]
                    if isinstance(response.get("context", []), list)
                    else str(response.get("context", "")),
        "answer": response.get("answer", "")
    }
    
    return response,safe_response

