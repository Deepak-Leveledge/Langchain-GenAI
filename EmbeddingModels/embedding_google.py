from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07",dimensions=32)

# result=model.embed_query("hello Deepak")

result=model.embed_documents(
    [
        "hello Deepak",
        "how are you doing?"
        "Where are you from?"

    ]
)
print(str(result))
print(len(result))
# print(result[0])