from langchain_community.vectorstores import FAISS
from langchain_google_genai import chat_models, GoogleGenerativeAIEmbeddings
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document


docs = [
    Document(
        page_content="""The Grand Canyon is one of the most visited natural wonders in the world.
Photosynthesis is the process by which green plants convert sunlight into energy.
Millions of tourists travel to see it every year. The rocks date back millions of years.""",
        metadata={"source": "Doc1"}
    ),
    Document(
        page_content="""In medieval Europe, castles were built primarily for defense.
The chlorophyll in plant cells captures sunlight during photosynthesis.
Knights wore armor made of metal. Siege weapons were often used to breach castle walls.""",
        metadata={"source": "Doc2"}
    ),
    Document(
        page_content="""Basketball was invented by Dr. James Naismith in the late 19th century.
It was originally played with a soccer ball and peach baskets. NBA is now a global league.""",
        metadata={"source": "Doc3"}
    ),
    Document(
        page_content="""LangChain is an AI platform that enables developers to build conversational AI applications.
It provides a range of tools and APIs for natural language processing and machine learning.""",
        metadata={"source": "Doc4"}
    ),
    Document(
        page_content="""LangChain's architecture is designed to be modular and extensible.
It allows developers to integrate their own models and algorithms into the platform.""",
        metadata={"source": "Doc5"}
    )
]

## create FAISSS

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")
vectorstore= FAISS.from_documents(docs, embeddings)



base_retriver= vectorstore.as_retriever(search_kwargs={"k": 5})


llm = chat_models.ChatGoogleGenerativeAI()
compressor = LLMChainExtractor.from_llm(llm)



compression_retriver=ContextualCompressionRetriever(
    base_retriever=base_retriver,
    base_compressor=compressor
)



quesry= "what is LangChain?"

compression_result= compression_retriver(quesry)


for i,doc in enumerate(compression_result):
    print(f"\n-- Result{i+1}")
    print(doc.page_content)