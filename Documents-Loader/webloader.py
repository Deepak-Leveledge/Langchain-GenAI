from langchain_community.document_loaders import WebBaseLoader
url="https://www.amazon.in/Machine-Learning-Absolute-Beginners-Introduction/dp/9362056860/ref=sr_1_5?dib=eyJ2IjoiMSJ9.VEO4rE6jLsq988MMZAzstykpIcSLcCFn6EQ0baJUh_V7RMF6VCHd5NzCOmk2KUvRQ7RAnkJVJUObRnH7mG8opsuoqo9Wc6wiCbNSCrcT6OD9fOvpKIxeaO5Z7gQ_3UVBeTlvMLXdOjcFyr3jtykO3A-LFTaEaCCnNJ21dCI90YIuNUU-5FWYe5-jX61sy9vr3fEiCBH7usa-72le4OOdUCWuXQZucRaDAvYLQenCRAg.bOwoI8Tz5L7cXlqM5IJ50mGUJMX9CcdmsStMVuLKC20&dib_tag=se&keywords=machine+learning+books&qid=1747463502&sr=8-5"
loader= WebBaseLoader(url)


docs =loader.load()

print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)