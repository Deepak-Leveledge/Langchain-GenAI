from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage



chat_template= ChatPromptTemplate([

    ('system','You are a helpful {domain} expert.'),
    ('human',"Explian in simple terms, what is {topic}")
    # SystemMessage(content="You are a helpful {domain} expert."),
    # HumanMessage(content="Explian in simple terms, what is {topic}")
])


prompt =chat_template.invoke({"domain":"AI","topic":"ChatGPT"})


print(prompt)