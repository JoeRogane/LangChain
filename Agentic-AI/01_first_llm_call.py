import requests
import json
 
# Ollama runs locally on port 11434
OLLAMA_URL = "http://localhost:11434/api/generate"
 
def ask_llm(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
 
    data = response.json()
    return data["response"]
 
if __name__ == "__main__":
    answer = ask_llm("What is an LLM in one sentence?")
    print(answer)