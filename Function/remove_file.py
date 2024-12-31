import os

def remove_file(file_path):
    max_attempts=3
    attempts=0
    while attempts < max_attempts:
        try:
            with open(file_path,"wb"):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"error : {e}")
            attempts +=1