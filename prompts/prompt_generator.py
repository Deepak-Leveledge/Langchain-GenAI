from langchain_core.prompts import PromptTemplate


#tempalte

template=PromptTemplate(
template="""
Please summarize the research paper titled "{paper_input}" with
Explanation Style: {style_input}
Explanation Length: {length_input}
1.Mathematical Details:
Include relevant mathematical equations if present in the
Explain the mathematical concepts using simple, intuitive
applicable.
2.Analogies:
Use relatable analogies to simplify complex ideas.
certain information is not available in the paper, respond
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided
""",
input_variables=["paper_input", "style_input", "length_input"],
validate_template=True
)



template.save("template.json")