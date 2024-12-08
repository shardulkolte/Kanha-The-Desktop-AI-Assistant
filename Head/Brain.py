import sys
import threading
import time
import webbrowser

from colorama import Fore
from wikipedia import summary, DisambiguationError, PageError  # Correct imports
from Head.Mouth import speak
from Traning_Model.model import mind

def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r'C:\FY MCA\Kanha\Data\brain_data\qna_data.txt'
qa_dict = load_qa_data(qa_file_path)

def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")

def print_animated_message(message):
    for char in message:
        color = Fore.YELLOW
        sys.stdout.write(color+char)
        sys.stdout.flush()
        time.sleep(0.05) #0.075 for slower animation
    print()

def wiki_search(prompt):
    search_prompt = prompt.replace("kanha", "").replace("wikipidia", "").strip()

    try:
        wiki_summary = summary(search_prompt, sentences=2)
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)


    except DisambiguationError as e:
        # Handle disambiguation error with suggestions
        message = "There are multiple results for your query. Please specify further."
        print_animated_message(message)
        speak(message)
        print("\nSuggestions:")
        for option in e.options[:5]:  # Show top 5 options
            print(f"- {option}")
    except PageError:
        google_search(prompt)

def google_search(query):
    query = query.replace("who is ", "").strip()
    if query:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        speak("You can see results for " + query + " in Google on your screen.")
        print("You can see results for " + query + " in Google on your screen.")
    else:
        speak("I didn't catch what you said.")
        print("I didn't catch what you said.")

def brain(text):
    try:
        response=mind(text)

        if not response:
            wiki_search(text)
            return

        animate_thread = threading.Thread(target=print_animated_message, args=(response,))
        speak_thread = threading.Thread(target=speak, args=(response,))
        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[text] = response
        save_qa_data(qa_file_path, qa_dict)

    except Exception as e:
        print(f"An error occured: {str(e)}")
        wiki_search(text)


