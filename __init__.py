__version__ = "rm-240522"


import libmineshaft.world
import pygame
import os


# TODO: Make the rendering engine manage the graphics implementation
# TODO: [PROGRESS] Partially done: Music is implemented
class Engine:
    def __init__(self, block_index, image_index):
        self.__version__ = __version__
        #if os.environ["SHOW_RENDER_VERSION"] == "1": #check if the enviroment variable "SHOW_RENDER_VERSION" is set to 1
        print(f"RenderMite v[{self.__version__}]")  # print the splash
        self.block_index = block_index
        self.image_index= image_index

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for x in range(0, 16):
            for y in range(0, 16): 
                block_contents = world.world[f"{x},{y}"].value
                block = self.block_index[block_contents["block_type"].value]()
                image =  pygame.image.load(os.path.join(self.assets_dir, "textures",  "terrain.png")).subsurface(block.imagecoords, (16,16))
                screen.blit(image, (pos[0]+x*16,  pos[1]+y*16))
