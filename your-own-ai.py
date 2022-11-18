from asyncio import *
import os
import openai
from art import *
with open('api.txt') as f:
    lines = f.read()
openai.api_key = (lines)


tprint ("\n\n\n\n -  Dr. CryTech  -")

print("\n\nHello i'm your artificial intelligence")
print("\nAsk me what you want, I can also give you multiple answers\n")

#Definizione
def risponde():
  domanda = input()
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt= (domanda),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(response.choices[0].text)

#Svolgimento programma
risponde()

while 1:
  print ("\nMe: ")
  risponde()
