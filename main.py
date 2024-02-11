from func.Listen import Listen
from func.Speak import Speak

from llm.GPT4 import ChatGpt
from llm.filter import Filter

import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!","I am Friday Sir. Please tell me how may I help you")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!","I am Friday Sir. Please tell me how may I help you")   

    else:
        Speak("Good Evening!","I am Friday Sir. Please tell me how may I help you")  


while 1:
    Query = Listen().lower()

    if 'gpt' in Query:
        response = ChatGpt(f"REPLY IN LESS WORDS {Query}")
        Speak(response)

    elif 'jarvis' in Query:
        code = ChatGpt(f"{Query} ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**")
        code = Filter(code)

        try:
            exec(code)
        except Exception as e:
            Speak("Sorry Sir geeting Some error.")

