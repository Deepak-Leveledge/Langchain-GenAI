from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

# Define the schema using TypedDict
class Review(TypedDict):
    summary: Annotated[str, "Summary of the review"]
    sentiment: Annotated[str, "Sentiment of the review"]

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1.0, max_completion_tokens=100)

# Apply the structured output with the defined schema
structured_model = model.with_structured_output(Review)

# Invoke the model with a sample review
result = structured_model.invoke("""
The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
""")

# Print the result and its type
print(result)
# print(type(result))


