from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message = "how to pass NCP-AII exam?"

resp = llm_gemini.invoke(message)

print(resp)
print(resp.content)