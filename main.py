import random
from Data.dlg_data.dlg import *
from Friday.fspeak import fspeak
from Function.check_online_ofline import realtime_online_checker
from Function.command import cmd


def check_kanha():
    text=realtime_online_checker()
    if "System status: ONLINE" in text:
        x = random.choice(online_dlg)
        fspeak(x)
        cmd()
    if "System status: NOT ONLINE" in text:
        x=random.choice(ofline_dlg)
        fspeak(x)

check_kanha()

