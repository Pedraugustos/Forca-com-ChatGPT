# funcoes que pedem a palavra ao ChatGPT

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_keyy = os.environ.get["OPENAI_API_KEY"]
print(api_keyy)
client = OpenAI(api_key = api_keyy)


def escolha_palavra():
    caracteres = input("Quantos caracteres vc deseja?")
    idioma = input("Qual idioma? ")
    dificuldade = input("Dificuldade: (0) Facil (1) Medio (2) Dificil ")
    temperature = float(dificuldade)
    
    prompt = [{"role":"user", "content": f"Gere uma palavra pra mim com {caracteres} caracteres, em {idioma} e em letras minusculas para um jogo da força"}]

    response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 1000,
    temperature = temperature
    )

    return response.choices[0].message.content