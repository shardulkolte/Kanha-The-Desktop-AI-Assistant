import threading
import edge_tts
from Function.play_audio import *
from Function.remove_file import remove_file

VOICE= "en-IN-PrabhatNeural" #Indian English, male
BUFFER_SIZE=1024
async def amain(TEXT,output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT,VOICE)
        await cm_txt.save(output_file)
        thread=threading.Thread(target=play_audio,args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print(f"error : {e}")
    finally:
        remove_file(output_file)