from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random

def bye():
    bye=random.choice(bye_key_word)
    speak(bye)