import libmineshaft.world
import pygame
import os


class Engine:
    def __init__(self, blockindex):
        self.__version__ = "unknown"
        print(f"RenderMite v[{self.__version__}]")
        self.blockindex = blockindex

    def render(self, screen, world: libmineshaft.world.World, pos=(0, 0)):
        for chunk in range(0, 16):
            for subchunk in range(0, 128):
                for block in range(0, 16):
                    block = self.blockindex[world.world[chunk][subchunk][block]]
                    if type(block.image) == list:
                        image = pygame.transform.scale(pygame.image.load(os.path.join(block.image)))
                        screen.blit(image, ((chunk + block) * 16, subchunk * 16))
                    elif block.image == False:
                        continue
