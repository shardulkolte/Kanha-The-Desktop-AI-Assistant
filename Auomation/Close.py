import random
import pyautogui as ui
from Data.dlg_data.dlg import closedlg
from Head.Mouth import speak

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random)
    ui.hotkey("alt","f4")