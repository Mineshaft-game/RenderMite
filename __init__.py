__version__ = "rm-240522"


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
        for x in range(0, 16):
            for y in range(0, 16): 
                block_contents = world.world[f"{x},{y}"].value
                block = self.blockindex[block_contents["block_id"].value]()
                image =  pygame.image.load(os.path.join(self.assets_dir, "textures",  "terrain.png")).subsurface(block.imagecoords, (16,16))
                screen.blit(image, (pos[0]+x*16,  pos[1]+y*16))
