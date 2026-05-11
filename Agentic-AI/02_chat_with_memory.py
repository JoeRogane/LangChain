import requests
 
# This list IS the memory. It grows with every turn.
conversation_history = []
 
def chat(user_message: str) -> str:
    global conversation_history
 
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
 
    payload = {
        "model": "llama3",
        "messages": conversation_history
    }
 
    url = "http://localhost:11434/api/chat"
    response = requests.post(url, json=payload)
    ai_reply = response.json()["message"]["content"]
 
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })
    return ai_reply
 
while True:
    user_input = input("You: ")
    if user_input == "quit": break
    reply = chat(user_input)
    print(f"AI: {reply}")