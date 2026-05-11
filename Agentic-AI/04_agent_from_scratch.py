import requests, json
 
# Define the tools the agent can use
def get_weather(city: str) -> str:
    return f"It's 22°C and sunny in {city}"
 
def calculate(expression: str) -> str:
    return str(eval(expression))
 
TOOLS = {"get_weather": get_weather, "calculate": calculate}
 
TOOL_DESCRIPTIONS = """
You have these tools:
- get_weather(city): Returns weather for a city
- calculate(expression): Evaluates a math expression
To use a tool, respond ONLY with JSON: {"tool": "name", "args": {"param": "value"}}
If no tool needed, answer directly."""
 
def run_agent(user_query: str) -> str:
    messages = [{"role": "system", "content": TOOL_DESCRIPTIONS}]
    messages.append({"role": "user", "content": user_query})
 
    for _ in range(5):  # max 5 agent steps
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "llama3", "messages": messages}
        ).json()["message"]["content"]
 
        try:
            tool_call = json.loads(response)
            tool_name = tool_call["tool"]
            tool_args = tool_call["args"]
            result = TOOLS[tool_name](**tool_args)
            messages.append({"role": "tool", "content": result})
        except json.JSONDecodeError:
            return response
    return "Max steps reached"
 
print(run_agent("What's the weather in London, and what's 42 * 7?"))