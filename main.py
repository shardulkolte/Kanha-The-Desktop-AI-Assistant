import random

from Data.dlg_data.dlg import *
from Friday.fspeak import fspeak
from Function.random_advice import get_random_advice
from Function.welcome import welcome
from Head.Mouth import *
from Head.Ear import *
from Head.Brain import *
from Function.wish import wish
from Function.bye import bye
from Traning_Model.model import mind
from Auomation.Open import open
from Auomation.Close import close
from Function.check_online_ofline import realtime_online_checker
import time


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

# def advice():
#     while True:
#         x = [5, 52, 58, 40, 30, 35, 67]
#         x = random.choice(x)
#         time.sleep(x)
#         speak("I have some suggestion for you, sakha.")
#         text = listen().lower()
#         if "yes tell me" in text or "yes" in text:
#             advice1 = get_random_advice()
#             speak(advice1)
#         else:
#             speak("no problem, i think you need some advice so i asked.")


# def kanha():
#     t1 = threading.Thread(target=cmd)
#     t2 = threading.Thread(target=advice())
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

def check_kanha():
    text=realtime_online_checker()
    if "System status: ONLINE" in text:
        x = random.choice(online_dlg)
        fspeak(x)
        kanha()
    if "System status: NOT ONLINE" in text:
        x=random.choice(ofline_dlg)
        fspeak(x)


check_kanha()
