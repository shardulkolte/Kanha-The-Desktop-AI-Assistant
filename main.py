from Data.dlg_data.dlg import wake_key_word, bye_key_word
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
        if text in wake_key_word:
            welcome()
        if text in bye_key_word:
            bye()
            break
        else:
            brain(text)

kanha()