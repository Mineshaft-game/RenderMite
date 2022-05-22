import io
import pygame

def load(file,  namehint = ""):
    if type(file) == str:
        return pygame.image.load(file)
    elif type(file) == io.TextIOWrapper:
        return pygame.image.load(file,  namehint)

def get_image_version():
    return pygame.image.get_sdl_image_version()
