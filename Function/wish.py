import datetime
from Head.Mouth import speak
import random
from Data.dlg_data.dlg import *


def wish():
    """
    Greets the user based on the current time of day.
    - Morning: 5:00 AM - 11:59 AM
    - Afternoon: 12:00 PM - 4:59 PM
    - Evening: 5:00 PM - 8:59 PM
    - Night: 9:00 PM - 4:59 AM
    """
    try:
        # Get the current time
        current_hour = datetime.datetime.now().hour

        # Determine the greeting based on the time
        if 5 <= current_hour < 12:
            chosen_message = random.choice(good_morningdlg)
            speak(chosen_message)
        elif 12 <= current_hour < 17:
            chosen_message = random.choice(good_afternoondlg)
            speak(chosen_message)
        elif 17 <= current_hour < 21:
            chosen_message = random.choice(good_eveningdlg)
            speak(chosen_message)
        else:
            chosen_message = random.choice(good_nightdlg)
            speak(chosen_message)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        speak(error_message)


# Example usage

