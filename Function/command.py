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
from Traning_Model.model2 import get_response


def cmd():
    wish()
    while True:
        text=listen().lower()

        if text in wake_key_word:
            welcome()
        if text in bye_key_word:
            bye()
            break
        elif text.startswith(("kanha","kana","gana")):
            text = text.replace("kanha", "")
            text = text.replace("kana", "")
            text = text.replace("gana", "")
            text = text.strip()
            response = get_response(text)
            speak(response)
        elif text.endswith(("kanha","kana","gana")):
            text = text.replace("kanha", "")
            text = text.replace("kana", "")
            text = text.replace("gana", "")
            text = text.strip()
            response = get_response(text)
            speak(response)
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
        elif "enter" in text or "press enter" in text or "send" in text or "enta" in text:
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

        # Sleep
        elif "sleep" in text or "system sleep karo" in text:
            speak("Putting the system to sleep...")
            gui.hotkey("win", "x")
            gui.press("u")
            gui.press("s")

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

        #scrolling
        elif "scroll up" in text or "upar scroll karo" in text:
            speak("Scrolling up...")
            gui.press('up', presses=10)
        elif "scroll down" in text or "neeche scroll karo" in text:
            speak("Scrolling down...")
            gui.press('down', presses=10)
        elif "scroll to top" in text or "shuruat par jao" in text or "scroll top" in text:
            speak("Scrolling to top...")
            gui.hotkey('home')
        elif "scroll to bottom" in text or "ant par jao" in text or "scroll bottom" in text:
            speak("Scrolling to bottom...")
            gui.hotkey('end')

        #note pad operations-------------------------------------------------------------------------
        # Open New Notepad
        elif "new notepad" in text or "naya notepad kholo" in text:
            speak("Opening a new Notepad...")
            gui.hotkey("ctrl", "n")


        # Write Something in Notepad
        elif "write" in text or "likho" in text or "right" in text:
            speak("Writing.")
            text = text.replace("write", "").replace("likho", "").replace("right", "")
            gui.write(text.strip())


        # Save File in Notepad
        elif "save file" in text or "notepad file save karo" in text or "save the file" in text:
            speak("Saving the file...")
            gui.hotkey("ctrl", "s")  # Save shortcut
            speak("What name should I save it as?")
            filename = listen().strip()  # Capture the file name
            if filename:
                gui.write(filename)
                gui.press("enter")
                speak(f"File saved as {filename}.")

        # Save As (for Renaming or Changing Location)
        elif "save as" in text or "save as karo" in text:
            speak("Saving the file with a new name...")
            gui.hotkey("ctrl", "shift", "s")  # Save As shortcut
            time.sleep(1)
            speak("What name should I save it as?")
            new_filename = listen().strip()  # Capture the new file name
            if new_filename:
                gui.write(new_filename)
                gui.press("enter")
                speak(f"File saved as {new_filename}.")

        # Close Notepad
        elif "close notepad" in text or "notepad band karo" in text:
            speak("Closing Notepad...")
            gui.hotkey("alt", "f4")

        # Delete All Content in Notepad
        elif "delete content" in text or "notepad ka content delete karo" in text:
            speak("Deleting all content...")
            gui.hotkey("ctrl", "a")  # Select all content
            gui.press("delete")  # Delete selected content


        # Undo Last Action in Notepad
        elif "undo" in text or "undo karo" in text:
            speak("Undoing last action...")
            gui.hotkey("ctrl", "z")

        # Redo Last Action in Notepad
        elif "redo" in text or "redo karo" in text:
            speak("Redoing last undone action...")
            gui.hotkey("ctrl", "y")

        # Find Text in Notepad
        elif "find text" in text or "text dhoondo" in text:
            speak("What should I search for?")
            search_query = listen().strip()  # Capture the text to search
            if search_query:
                gui.hotkey("ctrl", "f")  # Open Find dialog
                time.sleep(1)
                gui.write(search_query)
                gui.press("enter")
                speak(f"Searching for {search_query}.")

        # Replace Text in Notepad
        elif "replace text" in text or "text replace karo" in text:
            speak("What should I replace?")
            find_text = listen().strip()  # Capture the text to replace
            if find_text:
                speak("What should I replace it with?")
                replace_text = listen().strip()  # Capture the replacement text
                gui.hotkey("ctrl", "h")  # Open Replace dialog
                time.sleep(1)
                gui.write(find_text)
                gui.press("tab")  # Move to the replace field
                gui.write(replace_text)
                gui.press("enter")
                speak(f"Replaced {find_text} with {replace_text}.")

        # Select Specific Line
        elif "select line" in text or "line select karo" in text:
            speak("Which line number should I select?")
            line_number = listen().strip()
            if line_number.isdigit():
                for _ in range(int(line_number)):
                    gui.press("down")  # Move to the desired line
                gui.hotkey("shift", "home")  # Select the line
                speak(f"Selected line {line_number}.")

        # Cut Content
        elif "cut" in text or "cut karo" in text:
            speak("Cutting selected content...")
            gui.hotkey("ctrl", "x")

        # Delete File After Closing
        elif "delete file" in text or "file delete karo" in text:
            speak("Which file should I delete?")
            file_path = listen().strip()  # Capture the file path
            if file_path:
                gui.hotkey("win", "e")  # Open File Explorer
                time.sleep(1)
                gui.write(file_path)
                gui.press("enter")
                gui.hotkey("shift", "delete")  # Permanent delete
                gui.press("enter")  # Confirm deletion
                speak("File deleted successfully.")

        else:
            brain(text)
            # pass
