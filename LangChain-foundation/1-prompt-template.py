from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system":"You are an expert Gen-AI Engineer"),
        ("human":"Create a plan to pass {topic} first pass for {audience}")
    ]
)

#first step - build the prompt with variables
#second step - invoke the LLM

chain = prompt | llm_gemini #create a chain by piping prompt to LLM (LCEL)

variables = {
    "topic":" NVIDIA NCP-AAI",
    "audience":"Beginners"
}

resp = chain.invoke(variables)
print(resp)
print(resp.content)