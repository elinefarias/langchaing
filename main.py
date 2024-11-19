import config
from langchain.llms import OpenAI

api_key=config.OPENAI_API_KEY


llm = OpenAI(
  openai_api_key=api_key
)

result = llm(" Escreva um pequeno poema")
print(result)