import pygame

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound= pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        pygame.quit()

    except Exception as e:
        print(f"error : {e}")