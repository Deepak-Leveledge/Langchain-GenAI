from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_google_genai import ChatGoogleGenerativeAI


## creating Tools 
def get_conversion_factor(base_currency:str ,target_currency:str)->float:

    """
    fucntion fetches the currency conversion factor between base and targert currenct """

    url=f"https://v6.exchangerate-api.com/v6/cff257fb5e-0beabd6de1-swjyzo/pair/{base_currency}/{target_currency}"


    response=  requests.get(url)


    if response.json()["result"]== "error":
        raise ValueError("Invalid API KEY")

    return response.json()

@tool
def convert(base_currency:int,conversion_rate:float)-> float:

    """ given a currency conversion rate this function calculate the target currency value form a given base currency value """


    return base_currency * conversion_rate





# Correct function usage
rate = get_conversion_factor("USD", "INR")
print("Conversion Rate:", rate)

converted = convert(100, rate)
print("Converted Amount:", converted)



    
