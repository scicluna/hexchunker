##Spam out infinity islands/oceans with chatgpt
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

ISLANDNO = 5
rules = """I want you to generate a map of a fantasy continent using only these keys.
O is for ocean, representing every ocean hex. H is for hill, representing every hill hex. 
M is for mountain, representing every mountain hex. F is for forest. P is for plains.. 
Now using these characters in sequential order, build out a fantasy continent with realistic proportions
Each island should be unique.
"""

def generate_serially():
    llm = OpenAI(temperature=.9, openai_api_key=os.getenv('OPENAI_API_KEY'))
    prompt = PromptTemplate(
        input_variables=["rules"],
        template="Here are the rules: {rules}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for _ in range(ISLANDNO):
        resp = chain.run(rules=rules)
        print(resp)

generate_serially()
