import chromadb
import requests
 
client = chromadb.Client()
collection = client.create_collection("my_docs")
 
# Step 1: Chunk your document into pieces
documents = [
    "LLMs work by predicting the next token in a sequence.",
    "Docker containers package apps with all dependencies.",
    "Kubernetes orchestrates containers across multiple machines."
]
 
# Step 2: Embed & store in ChromaDB
collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3"]
)
 
def rag_answer(question: str) -> str:
    results = collection.query(
        query_texts=[question],
        n_results=2
    )
    context = " ".join(results["documents"][0])
 
    prompt = f"""Answer using only this context:
Context: {context}
Question: {question}"""
 
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]
 
print(rag_answer("How does Kubernetes work?"))