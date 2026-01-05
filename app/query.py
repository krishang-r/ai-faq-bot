import os
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

def get_local_ai_response(question):
    # 1. Setup Local Embeddings (Still using HuggingFace locally)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = FAISS.load_local("../data/faiss_index", embeddings, allow_dangerous_deserialization=True)
    
    # 2. Retrieve relevant context
    retrieved_docs = vector_db.similarity_search(question, k=3)
    context_text = "\n\n---\n\n".join([doc.page_content for doc in retrieved_docs])
    
    # 3. Construct the Local Prompt
    template = """
    You are a local AI assistant for "The Digital Bistro." 
    Answer the question based ONLY on the provided context.
    
    Context:
    {context}
    
    Question: {question}
    
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    # 4. Initialize Local LLM (Ollama)
    # Ensure Ollama app is running in the background!
    llm = OllamaLLM(model="llama3.1")
    
    # 5. Chain and Invoke
    chain = prompt | llm
    
    return chain.invoke({"context": context_text, "question": question})

if __name__ == "__main__":
    query = input("Ask Local Digital Bistro: ")
    print("\nLocal AI is thinking (using your Mac's GPU)...")
    print(f"\nResponse: {get_local_ai_response(query)}")