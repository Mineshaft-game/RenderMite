import pygame
import pygame.mixer

import os

def init_music():
    if pygame.mixer.get_init() is None:
        pygame.mixer.init()
        
        
def load_music(pathobj: os.PathLike):
    pygame.mixer.music.load(pathobj)
    
def play_music():
    pygame.mixer.music.play()
    
def stop_music():
    pygame.mixer.music.stop()
    
    
def unpause_music():
    pygame.mixer.music.unpause()
    
def set_volume(vol):
    pygame.mixer.music.set_volume(vol)
    
def get_volume():
    return pygame.mixer.music.get_volume()

def unload_music():
    pygame.mixer.music.unload()
    
def queue_music(pathobj: os.PathLike):
    pygame.mixer.music.queue(pathobj)
    
