from langchain.text_splitter import RecursiveCharacterTextSplitter ,Language

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


spliltter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0

)




chunks = spliltter.split_text(text)

print(len(chunks))
print(chunks[0])





print(chunks[0].page_content)
print(chunks[0].meta_data)

# print(chunks[0].page_content)
# print(chunks[0].meta_data)