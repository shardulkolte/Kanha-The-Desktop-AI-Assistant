# from fnmatch import translate
# import speech_recognition as sr
# import os
# import threading
# from mtranslate import translate
# import colorama
# from colorama import init,Fore,Style
#
# init(autoreset=True)
#
# def print_loop():
#     while True:
#         print(Fore.LIGHTGREEN_EX + "I am Listning...",end="",flush=True)
#         print(Style.RESET_ALL,end="",flush=True)
#         print("",end="",flush=True)
#
# def Trans_hindi_to_english(txt):
#     english_txt= translate(txt,to_language="en-in")
#     return english_txt
# def listen():
#     recognizer = sr.Recognizer()
#     recognizer.dynamic_energy_threshold=False
#     recognizer.energy_threshold=500
#     recognizer.dynamic_energy_adjustment_damping=0.02 #less more accurate for mic grasping energy
#     recognizer.dynamic_energy_ratio=1.9
#     recognizer.pause_threshold=0.4
#     recognizer.operation_timeout=None
#     recognizer.pause_threshold=0.4
#     recognizer.non_speaking_duration=0.4
#
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         while True:
#             print(Fore.LIGHTGREEN_EX + "I am Listning...", end="", flush=True)
#             try:
#                 audio= recognizer.listen(source,timeout=None)
#                 print("\r" + Fore.LIGHTYELLOW_EX + "Got it , Now Recognizing..",end="",flush=True)
#                 recognized_txt = recognizer.recognize_google(audio).lower()
#                 if recognized_txt:
#                     translated_txt = Trans_hindi_to_english(recognized_txt)
#                     print("\r"+ Fore.BLUE + "Shardul : " + translated_txt)
#                     return translated_txt
#                 else:
#                     return ""
#             except sr.UnknownValueError:
#                 recognized_txt = ""
#             finally:
#                 print("\r",end="",flush=True)
#
#             os.system("cls" if os.name == "nt" else "clear")
#             #threading part
#
#             listen_thread = threading.Thread(target=listen)
#             print_thread= threading.Thread(target=print_loop)
#             listen_thread.start()
#             print_thread.start()
#             listen_thread.join()
#             print_thread.join()

import speech_recognition as sr
import colorama
from colorama import init, Fore
from mtranslate import translate

from Head.Mouth import speak

# Initialize colorama for colored output
init(autoreset=True)

def translate_hindi_to_english(text):
    """
    Translate text from Hindi to English using mtranslate.
    """
    try:
        return translate(text, to_language="en-in")
    except Exception as e:
        print(Fore.RED + f"Translation error: {e}")
        return text  # Return original text if translation fails

def listen():
    """
    Listens to the user's voice, recognizes the text, and handles errors.
    """
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True  # Enable dynamic energy adjustment
    recognizer.energy_threshold = 300  # Fine-tuned for general usage
    recognizer.dynamic_energy_adjustment_damping = 0.03  # less more accurate for mic grasping energy
    recognizer.pause_threshold = 0.6  # Adjusted for better pause detection keep 1.0 for longer pause or keep 0.4 for less pause
    recognizer.non_speaking_duration = 0.4  # Minimum silence duration
    recognizer.operation_timeout = None  # No timeout limit

    with sr.Microphone() as source:
        print(Fore.LIGHTGREEN_EX + "Adjusting microphone for ambient noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        while True:
            print(Fore.LIGHTCYAN_EX + "I'm Listening... Speak now:")
            try:
                # Capture audio input
                audio = recognizer.listen(source, timeout=None,phrase_time_limit=10)
                print(Fore.LIGHTYELLOW_EX + "Processing your speech...")

                # Recognize and translate the speech
                recognized_text = recognizer.recognize_google(audio, language="hi-IN").lower()
                print(Fore.LIGHTGREEN_EX + f"Recognized Text: {recognized_text}")
                translated_text = translate_hindi_to_english(recognized_text)
                print(Fore.LIGHTBLUE_EX + f"Translated Text: {translated_text}")

                # Return the translated text
                return translated_text

            except sr.UnknownValueError:
                print(Fore.RED + "Sorry, I couldn't understand that. Please try again.")
                speak("Sorry, I couldn't understand that. Please try again.")
            except sr.RequestError as e:
                print(Fore.RED + f"Could not request results; {e}")
            except Exception as e:
                print(Fore.RED + f"An unexpected error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            print(Fore.MAGENTA + f"User said: {user_input}")
