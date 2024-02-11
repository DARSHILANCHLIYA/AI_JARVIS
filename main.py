from func.Listen import Listen
from func.Speak import Speak
from llm.GPT4 import ChatGpt


while 1:
    Query = Listen().lower()
    response = ChatGpt(f"REPLY IN LESS WORDS {Query}")
    Speak(response)



