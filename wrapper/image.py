import io
import pygame

def scale(image: pygame.Surface, size):
    return pygame.transform.scale(image,  size)

def subsurface(image,  pos,  image_size):
    return image.subsurface(pos, image_size)

def load(file,  namehint = ""):
    if type(file) == str:
        return pygame.image.load(file)
    elif type(file) == io.TextIOWrapper:
        return pygame.image.load(file,  namehint)

def get_image_version():
    return pygame.image.get_sdl_image_version()
