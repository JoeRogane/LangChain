from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import argparse
load_dotenv()

args= argparse.ArgumentParser(description:"Generate learning outline")
args.add_argument("--topic", type=str, required=True, help="Topic for learning outline")
args.add_argument("--audience", type=str, required=True, help="Target audience for learning outline")
parsed_args = args.parse_args()

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
    "topic": parsed_args.topic ,
    "audience":parsed_args.audience
}

resp = chain.invoke(variables)
print(resp)
print(resp.content)

#python 2-prompt-template.py --topic "NVIDIA NCP-AAI exam" --audience "beginners"