from langchain.text_splitter import RecursiveCharacterTextSplitter , Language


text="""
# A simple Python program to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    
    Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    
    return length * width

# Get input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_rectangle_area(length, width)

# Print the result
print("The area of the rectangle is:", area)"""



python_data_spillter= RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)



spit_text=python_data_spillter.split_text(text)
print(spit_text)    
print(len(spit_text))
print(spit_text[0])