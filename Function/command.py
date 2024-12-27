import time

from Data.dlg_data.dlg import *
from Function.welcome import welcome
from Head.Ear import *
from Head.Brain import *
from Function.wish import wish
from Function.bye import bye
from Traning_Model.model import mind
from Auomation.Open import open
from Auomation.Close import close
import pyautogui as gui

def cmd():
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

        elif "write" in text or "likho" in text or "right" in text:
            speak("Writing.")
            text = text.replace("write", "").replace("likho", "").replace("right", "")
            gui.write(text.strip())

        # Press Enter
        elif "enter" in text or "press enter" in text or "send" in text:
            gui.press("enter")

        # Select all
        elif "select all" in text or "select all paragraph" in text:
            gui.hotkey("ctrl", "a")

        # Copy
        elif "copy" in text or "copy this" in text:
            gui.hotkey("ctrl", "c")

        # Paste
        elif "paste" in text or "paste here" in text:
            gui.hotkey("ctrl", "v")

        # Undo
        elif "undo" in text or "undo karo" in text:
            gui.hotkey("ctrl", "z")

        # Copy last paragraph
        elif "copy last paragraph" in text:
            gui.hotkey("ctrl", "shift", "c")

        # Increase volume
        elif "increase volume" in text or "volume badhao" in text or "increase sound" in text:
            for _ in range(5):  # Increase volume 5 steps
                gui.press("volumeup")

        # Decrease volume
        elif "decrease volume" in text or "volume kam karo" in text or "decrease sound" in text:
            for _ in range(5):  # Decrease volume 5 steps
                gui.press("volumedown")

        # Mute/Unmute
        elif "mute" in text or "unmute" in text:
            gui.press("volumemute")

        # Maximize Window
        elif "maximize" in text or "maximize window" in text or "maximize karo" in text:
            speak("Maximizing the window...")
            gui.hotkey("win", "up")

        # Minimize Window
        elif "minimise" in text or "minimise the window" in text or "minimize karoge" in text or "minimize the window" in text:
            speak("Minimizing the window...")
            gui.hotkey('win', 'down')  # First down minimizes to half-screen
            gui.hotkey('win', 'down')  # Second down minimizes the window completely

        # Switch Tabs
        elif "switch tab" in text or "next tab" in text:
            speak("Switching tab...")
            gui.hotkey("ctrl", "tab")
        elif "previous tab" in text:
            speak("Switching to previous tab...")
            gui.hotkey("ctrl", "shift", "tab")

        # Open New Tab
        elif "new tab" in text or "open new tab" in text:
            speak("Opening new tab...")
            gui.hotkey("ctrl", "t")
        # Reopen previously closed Tab
        elif "reopen tab" in text or "open previously closed tab" in text:
            speak("Opening previously closed tab...")
            gui.hotkey("ctrl","shift", "t")

        # Close Tab
        elif "close tab" in text or "close this tab" in text:
            speak("Closing tab...")
            gui.hotkey("ctrl", "w")

        # Refresh Page
        elif "refresh" in text or "reload" in text:
            speak("Refreshing...")
            gui.hotkey("ctrl", "r")

        # Lock Screen
        elif "lock" in text or "lock screen" in text:
            speak("Locking screen...")
            gui.hotkey("win", "l")

        # Open Task Manager
        elif "task manager" in text or "open task manager" in text:
            speak("Opening task manager...")
            gui.hotkey("ctrl", "shift", "esc")

        # Take Screenshot
        elif "screenshot" in text or "take screenshot" in text:
            speak("Taking screenshot...")
            gui.hotkey("win", "prtsc")

        # Open File Explorer
        elif "file explorer" in text or "open file explorer" in text:
            gui.hotkey("win", "e")

        # Open Settings
        elif "settings" in text or "open settings" in text:
            gui.hotkey("win", "i")

        # Open Browser Menu
        elif "open browser menu" in text or "browser menu kholo" in text:
            gui.hotkey("alt")

        # Zoom In
        elif "zoom in" in text or "zoom in karo" in text:
            gui.hotkey("ctrl", "+")

        # Zoom Out
        elif "zoom out" in text or "zoom out karo" in text:
            gui.hotkey("ctrl", "-")

        # Open History
        elif "open history" in text or "history kholo" in text:
            gui.hotkey("ctrl", "h")

        # Open Bookmarks
        elif "open bookmarks" in text or "bookmarks kholo" in text:
            gui.hotkey("ctrl", "shift", "o")

        # Go Back
        elif "go back" in text or "peeche jao" in text:
            gui.hotkey("alt", "left")

        # Go Forward
        elif "go forward" in text or "aage jao" in text:
            gui.hotkey("alt", "right")

        # Open Dev Tools
        elif "open dev tools" in text or "dev tools kholo" in text:
            gui.hotkey("ctrl", "shift", "i")

        # Toggle Full Screen
        elif "toggle full screen" in text or "full screen karo" in text:
            gui.hotkey("f11")

        # Open Private Window
        elif "open private window" in text or "private window kholo" in text:
            gui.hotkey("ctrl", "shift", "n")

        #play, pause or stop
        elif "play" in text or "pause" in text or "stop" in text:
            gui.hotkey("space")
        elif text.startswith("search"):
            gui.hotkey("/")
            text=text.replace("search","")
            gui.write(text)
            speak(f"searching {text}")
            time.sleep(0)
            gui.press("enter")
        # Brightness Up
        elif "increase brightness" in text or "brightness badhao" in text:
            speak("Increasing brightness...")
            for _ in range(5):  # Increase brightness 5 steps
                gui.hotkey("fn", "f3")  # Adjust key based on your laptop

        # Brightness Down
        elif "decrease brightness" in text or "brightness kam karo" in text:
            speak("Decreasing brightness...")
            for _ in range(5):  # Decrease brightness 5 steps
                gui.hotkey("fn", "f2")  # Adjust key based on your laptop

        # Turn on Airplane Mode
        elif "turn on airplane mode" in text or "airplane mode on karo" in text:
            speak("Turning on Airplane mode...")
            gui.hotkey("win", "a")  # Open Action Center
            gui.press("tab", presses=4)  # Navigate to Airplane mode
            gui.press("space")

        # Turn off Airplane Mode
        elif "turn off airplane mode" in text or "airplane mode off karo" in text:
            speak("Turning off Airplane mode...")
            gui.hotkey("win", "a")  # Open Action Center
            gui.press("tab", presses=4)  # Navigate to Airplane mode
            gui.press("space")

        # Show Desktop
        elif "show desktop" in text or "desktop dikhaiye" in text:
            speak("Showing desktop...")
            gui.hotkey("win", "d")

        elif "increase speed" in text or "playback fast karo" in text:
            speak("Increasing playback speed...")
            gui.hotkey("ctrl", "shift", "right")
        elif "decrease speed" in text or "playback slow karo" in text:
            speak("Decreasing playback speed...")
            gui.hotkey("ctrl", "shift", "left")

        # Shutdown System
        elif "shutdown" in text or "system band karo" in text:
            speak("Shutting down the system...")
            gui.hotkey("win", "x")
            gui.press("u")
            gui.press("u")

        # Restart System
        elif "restart" in text or "system restart karo" in text:
            speak("Restarting the system...")
            gui.hotkey("win", "x")
            gui.press("u")
            gui.press("r")

        # Hibernate
        elif "hibernate" in text or "system hibernate karo" in text:
            speak("Hibernating the system...")
            gui.hotkey("win", "x")
            gui.press("u")
            gui.press("h")

        # Volume Mute Shortcut
        elif "mute volume" in text or "volume mute karo" in text:
            speak("Muting volume...")
            gui.hotkey("fn", "f6")  # Adjust key based on your laptop

        else:
            brain(text)
            # pass
