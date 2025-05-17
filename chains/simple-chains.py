from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from  langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

## creatin prompt
prompt=PromptTemplate(
    template="Generate 5 instresteing facts about {topic}",
    input_variables=["topic"]
)

## initiate model
model=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100)


## parser 

parser=StrOutputParser()



chain= prompt |model |parser


result=chain.invoke({'topic':'Deep Learning'})
# print(result)


chain.get_graph().print_ascii()

