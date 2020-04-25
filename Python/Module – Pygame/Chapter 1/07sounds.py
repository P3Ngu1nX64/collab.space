import pygame
import time

pygame.init()

# sound effects
soundObj = pygame.mixer.Sound('beeps.wav')
# use .unload() to free up resources
soundObj.play()

# stopping sound (sound runs in background)
time.sleep(2)
soundObj.stop()

# background music
# pygame can only load 1 background music simultaneously
pygame.mixer.music.load('terraria.mp3')
pygame.mixer.music.play(-1, 0.0)
# parameters: play(repetitions, start time) if repetitions is -1, loops forever
# start time is a float for seconds into the file to start playing.
time.sleep(2)
soundObj.play()
time.sleep(3)
pygame.mixer.music.stop()  # stops the loaded background music

pygame.mixer.music.unload()  # frees up resources

pygame.quit()  # uninitializes pygame

# Pygame sound effects can load WAV, MP3, and OGG files.
# Pygame background music can load WAV, MP3, and MIDI files.
