import libmineshaft.world
import pygame
import os


def joinpath(path: list):
    returnstr = str()
    for entry in path:
        returnstr = returnstr + os.path.sep + entry
        
    return os.fspath(returnstr)

#TODO: Make the rendering engine manage the graphics implementation
class Engine:
    def __init__(self, blockindex):
        self.__version__ = "unknown"
        if os.environ["SHOW_RENDER_VERSION"] == "1": #check if the enviroment variable "SHOW_RENDER_VERSION" is set to 1
            print(f"RenderMite v[{self.__version__}]") #If yes, print the splash
        self.blockindex = blockindex 

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for chunk in range(0, 16): # For every chunk
            for subchunk in range(0, 128): #For every subchunk
                for block in range(0, 16): # for every block
                    block = self.blockindex[world.world[chunk][subchunk][block]]
                    if type(block.image) == list:
                        image = pygame.transform.scale(pygame.image.load(joinpath(block.image)))
                        screen.blit(image, ((chunk + block) * 16, subchunk * 16))
                    elif block.image == False:
                        continue
