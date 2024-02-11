from func.Listen import Listen
from func.Speak import Speak

from llm.GPT4 import ChatGpt
from llm.filter import Filter

import datetime , time

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!","I am Friday Sir. Please tell me how may I help you")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!","I am Friday Sir. Please tell me how may I help you")   

    else:
        Speak("Good Evening!","I am Friday Sir. Please tell me how may I help you")  

wishMe()

Previous_Chat = open(r"D:\Jarvis\JARVIS\data\chat.txt", "r")
Previous_Chat = Previous_Chat.read()

ChatGpt(f"Our prevoius chat Chat now according to this{Previous_Chat}. NOTE don't reply only for this command. I gave you this command to just rember past chats")

time.sleep(3)

while 1:
    Query = Listen().lower()

    if 'delet' in Query and 'chat' in Query:

        Speak("Deleting all memory sir")
        
        file_delet = open("D:\Jarvis\JARVIS\data\chat.txt", "w")
        file_delet.write("")
        file_delet.close() 

        Speak("Sir now All conversation of us is deleted")

    elif 'gpt' in Query:

        Query = Query.replace("gpt",'')
        begin = time.time()

        response = ChatGpt(f"REPLY IN LESS WORDS {Query}")
        end = time.time()

        print(end - begin)
        Speak(response)

        f = open("D:\Jarvis\JARVIS\data\chat.txt", "a")
        f.writelines(f"YOU:  {Query}\n")
        f.writelines(f" AI:  {response}\n")
        f.close()        

    elif 'jarvis' in Query:
        

        begin = time.time()

        Query = Query.replace("jarvis","")
        code = ChatGpt(f"{Query} ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**")
        code = Filter(code)

        try:
            exec(code)
            end = time.time()

            print(end - begin)
        except Exception as e:
            Speak("Sorry Sir getting Some error.")
            
