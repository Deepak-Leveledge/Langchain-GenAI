import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
load_dotenv()


from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

@tool
def get_weather(city:str)-> str:
    """
    fucntion fetches the weather information for a given city
    """
    url=f"https://api.weatherstack.com/current?access_key=4d1dBae207aBcB45a52df8a623e&query={city}"

    response=  requests.get(url)

    # if response.json()["result"]== "error":
    #     raise ValueError("Invalid API KEY")

    return response.json()



search_tool =DuckDuckGoSearchRun()





# result=search_tool.invoke("top news in india today")
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0)
llm_result=llm.invoke("Hello how are you")
# print("LLM Result:",llm_result)
# print(result)



##pulling the teact agent 
prompt= hub.pull("hwchase17/react")
# print(prompt)


## crating the react agent manually

agent= create_react_agent(
    llm=llm,
    tools=[search_tool,get_weather],
    prompt=prompt
)

## wrap it with Agent excautor 

agent_executor= AgentExecutor(
    agent=agent,
    tools=[search_tool,get_weather],
    verbose=True,
)


# invoke the agent executor

result= agent_executor.invoke({"input":"what is the capital of inida? and what is the weather of capital of india?"})
# print(result)
print(result['output'])   