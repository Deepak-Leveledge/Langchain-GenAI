from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from  langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Optional,Literal
load_dotenv()





model= ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100)

parser= StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] =Field(description="Sentiment of the review")


parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1=PromptTemplate(
    template="classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)


classifier_chain=prompt1 | model | parser2

# result=classifier_chain.invoke({"feedback":"The product is terible"}).sentiment
# print(result)


prompt2=PromptTemplate(
    
    template="Write the appropriate response to this positive feedback \n {feedback} ",
    input_variables=["feedback"]
)

prompt3=PromptTemplate(
    
    template="Write the appropriate response to this negative feedback \n {feedback} ",
    input_variables=["feedback"]
)





branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt2 | model | parser),
    (lambda x:x.sentiment=="negative",prompt3 | model | parser),
    RunnableLambda(lambda x:"unknown sentiment")


)



merge_chain= classifier_chain | branch_chain



result=merge_chain.invoke({"feedback":"The product is terible"})

print(result)
merge_chain.get_graph().print_ascii()