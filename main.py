from Data.dlg_data.dlg import *
from Function.welcome import welcome
from Head.Mouth import *
from Head.Ear import *
from Head.Brain import *
from Function.wish import wish
from Function.bye import bye
from Traning_Model.model import mind
from Auomation.Open import open
from Auomation.Close import close



def kanha():
    wish()
    while True:
        text=listen().lower()

        if text in wake_key_word:
            welcome()
        if text in bye_key_word:
            bye()
            break
        elif text.startswith(("open","kholo","show me")):
            text = text.replace("kholo", "")
            text = text.replace("show me", "")
            text = text.strip()
            open(text)
        elif text in open_input:
            text = text.replace("big", "")
            text = text.replace("kholo", "")
            text = text.replace("khologe", "")
            text = text.strip()
            open(text)
        elif text in close_input:
            close()
        else:
            brain(text)
            # pass

kanha()