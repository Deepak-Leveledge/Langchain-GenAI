from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from  langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()


model1= ChatGoogleGenerativeAI(model="gemini-2.0-flash",max_tokens=150)


model2= ChatGoogleGenerativeAI(model="gemini-2.0-flash",max_tokens=150)

prompt1= PromptTemplate(
    template="generate a short and simple notes from the follwing text \n{text}",
    input_variables=["text"]
)

prompt2=PromptTemplate(
    template="Generate  5 short question answers from the follwing text  \n{text}",
    input_variables=["text"]
)


prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a single Document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes","quiz"]
)


parser = StrOutputParser()


parallel_chain= RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})



merge_chain = prompt3 | model1 |parser

chain =parallel_chain | merge_chain


text ="""
Linear regression is a type of supervised machine-learning algorithm that learns from the labelled datasets and maps the data points with most optimized linear functions which can be used for prediction on new datasets. It assumes that there is a linear relationship between the input and output, meaning the output changes at a constant rate as the input changes. This relationship is represented by a straight line.

For example We want to predict a student's exam score based on how many hours they studied. We observe that as students study more hours, their scores go up. In the example of predicting exam scores based on hours studied. Here

    Independent variable (input): Hours studied because it's the factor we control or observe.
    Dependent variable (output): Exam score because it depends on how many hours were studied.

We use the independent variable to predict the dependent variable.
How-Linear-Regression-Works_.webpHow-Linear-Regression-Works_.webp
Why Linear Regression is Important?

Here’s why linear regression is important:

    Simplicity and Interpretability: It’s easy to understand and interpret, making it a starting point for learning about machine learning.
    Predictive Ability: Helps predict future outcomes based on past data, making it useful in various fields like finance, healthcare and marketing.
    Basis for Other Models: Many advanced algorithms, like logistic regression or neural networks, build on the concepts of linear regression.
    Efficiency: It’s computationally efficient and works well for problems with a linear relationship.
    Widely Used: It’s one of the most widely used techniques in both statistics and machine learning for regression tasks.
    Analysis: It provides insights into relationships between variables (e.g., how much one variable influences another).

Best Fit Line in Linear Regression

In linear regression, the best-fit line is the straight line that most accurately represents the relationship between the independent variable (input) and the dependent variable (output). It is the line that minimizes the difference between the actual data points and the predicted values from the model.
"""

result=chain.invoke({"text":text})
print(result)

# chain.get_graph().print_ascii()






