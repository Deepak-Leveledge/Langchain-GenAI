from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv



loader= DirectoryLoader(
    path="allpdf",
    glob='*.pdf',
    loader_cls= PyPDFLoader


)

docs= loader.load()


for documents in docs:
    print(documents.page_content)

