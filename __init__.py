
__version__ = "unknown"


import libmineshaft.world
import pygame
import os


def joinimagepath(path: list,  assets_dir: str): 
    returnstr = assets_dir
    for entry in path:
        returnstr = returnstr + os.path.sep + entry
        print(returnstr)

    return returnstr


# TODO: Make the rendering engine manage the graphics implementation
class Engine:
    def __init__(self, blockindex,  assets_dir):
        self.__version__ = __version__
        # if os.environ["SHOW_RENDER_VERSION"] == "1": #check if the enviroment variable "SHOW_RENDER_VERSION" is set to 1
        print(f"RenderMite v[{self.__version__}]")  # print the splash
        self.blockindex = blockindex
        self.assets_dir = assets_dir

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for chunk in range(0, 16):  # For every chunk
            for subchunk in range(0, 128):  # For every subchunk
                for block in range(0, 16):  # for every block
                    block = self.blockindex[world.world[chunk][subchunk][block]]
                    if type(block.image) is list:

                        path = joinimagepath(block.image,  self.assets_dir)
                        print(path)
                        image = pygame.transform.scale(pygame.image.load(path),  (16, 16))
                        screen.blit(image, (16 * 16, subchunk * 16))
                    elif block.image is False:
                        continue
