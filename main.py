import random
from Data.dlg_data.dlg import *
from Friday.fspeak import fspeak
from Function.check_online_ofline import realtime_online_checker
from Function.command import cmd


# def kanha():
#     t1 = threading.Thread(target=cmd())
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
        cmd()
    if "System status: NOT ONLINE" in text:
        x=random.choice(ofline_dlg)
        fspeak(x)


check_kanha()

# import random
# import time
# from threading import Event
# from concurrent.futures import ThreadPoolExecutor
# from Data.dlg_data.dlg import *
# from Friday.fspeak import fspeak
# from Function.random_advice import get_random_advice
# from Function.welcome import welcome
# from Head.Mouth import *
# from Head.Ear import *
# from Head.Brain import *
# from Function.wish import wish
# from Function.bye import bye
# from Traning_Model.model import mind
# from Auomation.Open import open
# from Auomation.Close import close
# from Function.check_online_ofline import realtime_online_checker
#
# stop_event = Event()
#
# def cmd():
#     """Main command loop for listening and responding to user input."""
#     wish()
#     while not stop_event.is_set():  # Check if the stop event is triggered
#         text = listen().lower()
#
#         if text in wake_key_word:
#             welcome()
#         elif text in bye_key_word:
#             bye()
#             stop_event.set()  # Trigger stop event to terminate threads
#             break
#         elif text.startswith(("open", "kholo", "show me")):
#             text = text.replace("kholo", "").replace("show me", "").strip()
#             open(text)
#         elif text in open_input:
#             text = text.replace("big", "").replace("kholo", "").replace("khologe", "").strip()
#             open(text)
#         elif text in close_input:
#             close()
#         else:
#             brain(text)
#
#
# def advice():
#     """Provide random advice periodically."""
#     while not stop_event.is_set():  # Check if the stop event is triggered
#         delay = random.randint(20, 60)  # Random delay between advice prompts
#         time.sleep(delay)
#         if stop_event.is_set():  # Double-check before proceeding
#             break
#         speak("I have some suggestions for you, Sakha.")
#         text = listen().lower()
#         if "yes tell me" in text or "yes" in text:
#             advice_text = get_random_advice()
#             speak(advice_text)
#         else:
#             speak("No problem, I thought you might need some advice.")
#
#
# def kanha():
#     """Run the command and advice modules in parallel."""
#     with ThreadPoolExecutor(max_workers=2) as executor:
#         executor.submit(cmd)
#         executor.submit(advice)
#
#
# def check_kanha():
#     """Check system status and initialize Kanha."""
#     status = realtime_online_checker()
#     if "System status: ONLINE" in status:
#         fspeak(random.choice(online_dlg))
#         kanha()
#     else:
#         fspeak(random.choice(ofline_dlg))
#
#
# # Run the program
# if __name__ == "__main__":
#     check_kanha()
