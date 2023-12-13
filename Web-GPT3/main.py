import openai
import os

from secrets_1 import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(engine="text-davinci-001", prompt="Digamos que esto es una prueba", max_tokens=6)
print(response)

