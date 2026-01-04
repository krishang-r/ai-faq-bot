import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def ask_bot(question):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = FAISS.load_local("../data/faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = vector_db.similarity_search(question, k=3)
    
    return docs

if __name__ == "__main__":
    user_query = input("Ask a question about the restaurant: ")
    results = ask_bot(user_query)
    
    print("\n--- Top Relevant Chunks ---")
    for i, doc in enumerate(results):
        print(f"\nResult {i+1}:")
        print(doc.page_content)