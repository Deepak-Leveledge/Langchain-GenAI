from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model= ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100)



loader= PyPDFLoader("allpdf/DROW.pdf")
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)