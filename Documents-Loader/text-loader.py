from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model= ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100)


prompt =PromptTemplate(
    template="Write a summary for th follwiong poem -\n {poem}",
    input_variables=["poem"]
)

parser= StrOutputParser()


loader= TextLoader("data.txt",encoding="utf-8")

docs= loader.load()
# print(docs)
# print(type(docs))
# print(len(docs))
# print(type(docs[0]))
# print(docs)


chain=  prompt | model | parser
print(chain.invoke({"poem":docs[0].page_content}))