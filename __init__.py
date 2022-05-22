__version__ = "unknown"


import libmineshaft.world
import pygame
import os


def joinimagepath(path: list, assets_dir: str):
    returnstr = assets_dir
    for entry in path:
        returnstr = returnstr + os.path.sep + entry
        print(returnstr)

    return returnstr


# TODO: Make the rendering engine manage the graphics implementation
# TODO: [PROGRESS] Partially done: Music is implemented
class Engine:
    def __init__(self, blockindex, assets_dir):
        self.__version__ = __version__
        # if os.environ["SHOW_RENDER_VERSION"] == "1": #check if the enviroment variable "SHOW_RENDER_VERSION" is set to 1
        print(f"RenderMite v[{self.__version__}]")  # print the splash
        self.blockindex = blockindex
        self.assets_dir = assets_dir

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for x in range(pos[0] - screen.width()/2):
            for y in range(pos[1] + screen.width()/2): 
                pass
                block_type,  block_data,  x, y=world.database.execute("SELECT * FROM blocks WHERE x=? AND y=?", (x,y))
                block = self.blockindex[0]()
                image =  pygame.subsurface(pygame.image.load(os.path.join(self.assets_dir, "terrain.png")), block.imagecoords, (16,16))
                screen.blit(image, ())
