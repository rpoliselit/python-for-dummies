"""
Make a script that opens and runs an mp3 file by using pygame lib.
"""

import pygame

pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

pygame.init()
pygame.mixer.music.load('022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
