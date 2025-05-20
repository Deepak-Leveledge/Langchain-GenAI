
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import MMRRetriever
from langchain_community.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document

docs=[
    Document(page_content="Langchian make it easy to work with LLMs"),
    Document(page_content="Langchian is used to build LLm based applications"),
    Document(page_content="Langchian is used to build LLM based applications"),
    Document(page_content="Langchian is used to build LLM based applications"),
    Document(page_content="Langchian is used to build LLM based applications"),
   ]



embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)



retriver =vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2,"lambda_mult": 0.5}
)


quert= "What is langchian"

result= retriver.invoke(quert)
print(result)


