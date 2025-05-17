from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07",dimensions=32)


documents=[
    "Virat Kohli  is a India cricketer",
    "MS Dhoni is a India cricketer and he is captain of India",
    "Rohit Sharma is a India cricketer  and he is a bastman",
    "jasprit bhumra is a India cricketer and he is a allrounder",
    "jadeja is a India cricketer and he is a allrounder",
]

query="who is the best allrounder in india"


document_embeding = embedding.embed_documents(documents)
query_embeding = embedding.embed_query(query)

score=cosine_similarity([query_embeding], document_embeding)[0]

# index,score=(list(enumerate(score)),key=lambda x:x[1])
index,score=(sorted(list(enumerate(score)),key=lambda x:x[1])[-1])

print(query)
print(documents[index])
print("similarity score",score)


