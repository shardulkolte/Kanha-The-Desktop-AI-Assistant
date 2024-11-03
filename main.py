from Function.welcome import welcome
from Head.Mouth import *
from Head.Ear import *
from Head.Brain import *
from Function.wish import wish
from Function.bye import bye



def kanha():
    wish()
    while True:
        text=listen().lower()
        if "krishna" in text:
            welcome()
        if "bye" in text:
            bye()
            break
        else:
            brain(text)

kanha()