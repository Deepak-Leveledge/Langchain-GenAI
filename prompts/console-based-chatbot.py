from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1.0,max_completion_tokens=100)


chat_history=[
    SystemMessage(content="You are a helpful assistant."),
]


while True:
    user_input= input("You:-")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI Bot:-",result.content)
print(chat_history)


# result=model.invoke("Write the poem on love?")
# print(result.content)