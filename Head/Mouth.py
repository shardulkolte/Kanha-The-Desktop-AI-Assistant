import asyncio
from Function.amain import *
import os

def speak(TEXT,output_file=None):
    if output_file is None:
        output_file=f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT, output_file))





