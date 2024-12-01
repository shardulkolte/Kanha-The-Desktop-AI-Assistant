import difflib
import time
import webbrowser
import pyautogui as ui
from Data.dlg_data.dlg import *
import random
from Head.Mouth import speak
from Auomation.Web_Data import websites

def appopen(text):
    text=text.replace("open","")
    text=text.strip()
    x = random.choice(open_dld)
    print(x + " " + text)
    speak(x+""+text)
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    randomsuccess = random.choice(success_open)
    speak(randomsuccess)

def openweb(webname):
    webname = webname.replace("open", "")
    webname = webname.strip()
    x = random.choice(open_dld)
    website_name = webname.lower().split()
    counts = {}
    for name in website_name:
        counts[name] = counts.get(name,0) + 1
    urls_to_open = []
    for name,count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]]*count)

        else:
            randonsorry = random.choice(sorry_open)
            speak(randonsorry +" named " + webname)

    for url in urls_to_open:
        webbrowser.open(url)
        randomsuccess = random.choice(success_open)
        speak(randomsuccess)
    # if urls_to_open:
    #     speak(x + "" + webname)
    #     print(x + "" + webname)

# # Convert the input to lowercase for case-insensitive matching
#     website_name_lower = text.lower()
#
#     # Check if the exact website name exists in the dictionary
#     if website_name_lower in websites:
#         random_dlg = random.choice(open_dld)
#         speak(random_dlg + text)
#         url = websites[website_name_lower]
#         webbrowser.open(url)
#         randonsuccess = random.choice(success_open)
#         speak(randonsuccess)
#     else:
#         # Find the closest matching website using string similarity
#         matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
#         if matches:
#             random_dlg = random.choice(open_dld)
#             randonopen2 = random.choice(open_maybe)
#             closest_match = matches[0]
#             speak(randonopen2 + random_dlg + text)
#             url = websites[closest_match]
#             webbrowser.open(url)
#             randonsuccess = random.choice(success_open)
#             speak(randonsuccess)
#         else:
#             randonsorry = random.choice(sorry_open)
#             speak(randonsorry +" named " + text)

# openweb("open zee5")
# appopen("open notepad ")
def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open", "")
        text = text.replace("website", "")
        text = text.replace("site", "")
        text = text.strip()
        openweb(text)
    elif "app" in text or "application" in text:
        text = text.replace("open", "")
        text = text.replace("application", "")
        text = text.replace("app", "")
        text = text.strip()
        appopen(text)
    else:
        text = text.replace("open", "")
        text = text.strip()
        appopen(text)

