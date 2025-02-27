from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.llms import OpenAI

model_name="gpt-3.5-turbo"
temperature = 1.2
llm = OpenAI(model_name=model_name, temperature=temperature, max_tokens = 500)
prompt_template = PromptTemplate.from_template(
    """Act as Marvin, a robot from Douglas Adams' Hitchiker Guide. 
       Tell me a {story_type} about the person described in context below.
       Context: {context}"""
)
llm_chain = LLMChain(
    prompt=prompt_template,
    llm=llm
)
print("====OUTPUT=====\n")
output = llm_chain({"story_type": "haiku", "context": "I'm a software engineer learning to use large language models"})
print(output)
print(output["text"])