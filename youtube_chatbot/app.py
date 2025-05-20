import os 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import re
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnablePassthrough,RunnableLambda ,RunnableParallel
from langchain_core.output_parsers  import StrOutputParser

from dotenv import load_dotenv
load_dotenv()




st.title("YouTube Video Chatbot 🤖")
st.header("Enter the YouTube video ID  to get started!")
# video_id = st.text_input("Enter the YouTube video URL")

video_id = st.text_input("Enter the YouTube video ID")
if not video_id:
    st.warning("Please enter a valid video ID.")
    st.stop()

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','hi'])

    text= " ".join(chunk["text"] for chunk in transcript)

except Exception as e:
    st.error("Transcript nahi mil paaya. Check karein ki video public hai aur  transcript available hai.")
    st.stop()

with st.expander("Show Transcript"):
    st.write(text)

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
chunks = splitter.create_documents([text])
st.write("splitted chunks:", len(chunks))


with st.expander("Chunks Preview"):
    for idx, chunk in enumerate(chunks[:3]):
        st.write(f"Chunk {idx+1}:", chunk.page_content)



# embeddings and vectorstore
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_type="similarity",search_kwargs={"k": 5})

## llm and prompt
llm= ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1.0)

prompt= PromptTemplate(
        template="""Your are a help full assitant.
    Answer Only from the provided transcript context.
    if the context is insufficient ,just say you dont know.
    context:{context}
    Question:{question}""",
    input_variables=["context","question"],
    )


    


question = st.text_input("Ask a question about the video:")
    
if question:
     with st.spinner("Generating response..."):
        # 1. Retrieve relevant chunks
        relevant_docs = retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)

        # 2. Build chat messages
        messages = [
            SystemMessage(content="You are a helpful assistant. Answer only from the provided context."),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion:\n{question}")
        ]

        # 3. Invoke LLM
        ai_message = llm.invoke(messages)

        # 4. Display answer
        st.write("Answer:", ai_message.content)
else:
    st.warning("Please enter a question to get a response.")
        

#     relevant_docs = retriever.get_relevant_documents(question)
#     context_text = "\n\n".join(doc.page_content for doc in relevant_docs)



#     response = llm(prompt.format(context=context_text, question=question))



    
#     def format_response(retriever, question):
#         context_text ="\n\n ".join(doc.page_content for doc in retriver.get_relevant_documents(question))



    
#     parallel_chain = RunnableParallel({
#     "context":retriver | RunnableLambda(format_response),
#     "question":RunnablePassthrough()
#    })
    


#     parser= StrOutputParser()


#     main_chain=  parallel_chain | prompt | llm | parser






    
    

    






    

    



