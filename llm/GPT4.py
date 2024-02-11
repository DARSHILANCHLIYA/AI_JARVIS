#pip install -U g4f
import g4f
#can we talk on call ?  
from time import time as t

messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Divyansh Shukla with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "system", "content": """```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="iron man")
print(IMGS)
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
IMGS_TO_SHOW.open(1)
```
```python
from func.Jukebox.YouTube import MusicPlayer
#taks song name and it stats playing music
ncs=MusicPlayer("ncs")
#any btw 0 - 100
ncs.Vol(30)
#pause or play
ncs.Play()
ncs.Pause()
#next song
ncs.Next()
#quit song
ncs.Quit()
     """},
    {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
    {"role": "assistant", "content": """```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
    {"role": "user", "content": "Jarvis show me the next image"},
    {"role": "assistant", "content": """```python
IMGS_TO_SHOW.open(1)
```"""},
    {"role": "user", "content":"Jarvis play neffex cold"},
    {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""}
]

def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x>5500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None

def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    MsgDelAuto()
    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})


    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})

    return ms

if __name__=="__main__":
    Previous_Chat = open(r"D:\Jarvis\JARVIS\data\chat.txt", "r")
    Previous_Chat = Previous_Chat.read()
        
    ChatGpt(f"Our prevoius chat Chat now according to this{Previous_Chat}. NOTE don't reply only for this command. I gave you this command to just rember past chats")

    while 1:
        A=input(">>> ")
        C=t()
        response_GPT = ChatGpt(A)
        print(t()-C)

        f = open("D:\Jarvis\JARVIS\data\chat.txt", "a")
        f.writelines(f"YOU:  {A}\n")
        f.writelines(f" AI:  {response_GPT}\n")
        f.close()
