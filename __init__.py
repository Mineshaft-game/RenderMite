__version__ = "unknown"


import libmineshaft.world
import pygame
import os


# TODO: Make the rendering engine manage the graphics implementation
# TODO: [PROGRESS] Partially done: Music is implemented
class Engine:
    def __init__(self, blockindex, assets_dir):
        self.__version__ = __version__
        #if os.environ["SHOW_RENDER_VERSION"] == "1": #check if the enviroment variable "SHOW_RENDER_VERSION" is set to 1
        print(f"RenderMite v[{self.__version__}]")  # print the splash
        self.blockindex = blockindex
        self.assets_dir = assets_dir

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for x in range(0, 256):
            for y in range(0, 128): 
                world.database.execute("SELECT * FROM world WHERE x=? AND y=?", (x,y))
                block_type,  block_data,  x, y=world.database.fetchall()[0]
                block = self.blockindex[block_type]()
                image =  pygame.subsurface(pygame.image.load(os.path.join(self.assets_dir, "terrain.png")), block.imagecoords, (16,16))
                screen.blit(image, (pos+x*16,  pos+y*16))
