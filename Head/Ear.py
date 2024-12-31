import speech_recognition as sr
import colorama
from colorama import init, Fore,Style,init
from mtranslate import translate

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
    recognizer.dynamic_energy_adjustment_damping = 0.013  # less more accurate for mic grasping energy
    recognizer.pause_threshold = 0.6  # Adjusted for better pause detection keep 1.0 for longer pause or keep 0.4 for less pause
    recognizer.non_speaking_duration = 0.4  # Minimum silence duration
    recognizer.operation_timeout = None  # No timeout limit


    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTCYAN_EX +"I am Listening...", end="", flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r"+Fore.LIGHTYELLOW_EX + "Processing your speech...",end="",flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    print("\r"+Fore.LIGHTGREEN_EX + f"Sakha: {recognized_txt}")
                    return recognized_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)


