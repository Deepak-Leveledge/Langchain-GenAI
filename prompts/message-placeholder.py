from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage

from langchain_core.embeddings import OpenAIEmbeddings


## message place holder is used to  add the previous converstaion of human and ai  in the new converstaion due to that ai will not forgate what user is asking 
## chat template

chat_template= ChatPromptTemplate.from_messages([
    ('System',"You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history")
    ('Human',"{query}")
    
])

chat_history=[]


#load chat history 

with open("chat_history.txt","r") as f:
    chat_history.extend(f.readlines())

print(chat_history)


##create prompt
chat_template.invoke({"chat_history":chat_history,"query":"where is my refund?"})

