from func.Listen import Listen
from func.Speak import Speak

while 1:
    Query = Listen().lower()
    if 'hello' in Query:
        Speak("Hello")