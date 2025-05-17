from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from  langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1= PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=["topic"]
)


prompt2=PromptTemplate(
    template="Generate a 5 pointer summary from the follwoing text \n {text}",
    input_variables=["text"]
)


model= ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100
                              )


parser = StrOutputParser()


chain = prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"topic":"Deep Learning"})
print(result)


chain.get_graph().print_ascii()
