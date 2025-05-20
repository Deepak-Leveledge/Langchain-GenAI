from langchain_core.tools import tool

# def multiply(a,b):
#     """multiply of two numbers"""
#     return a*b


# ## type hinting 
# def multiplt(a:int ,b:int)-> int:
#     """multiply of two numbers"""
#     return a*b




@tool
def multiplt(a:int ,b:int)-> int:
    """multiply of two numbers"""
    return a*b



result= multiplt({"a":5,"b":6})
print(result)
print(result.name)
print(result.description)
print(result.args)


