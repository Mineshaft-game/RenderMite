import libmineshaft
import pygame


class Engine:
    def __init__(self, blockindex):
        self.blockindex = blockindex

    def render(self, screen, world, pos=(0, 0)):
        for chunk in range(0, 16):
            for subchunk in range(0, 225):
                for block in range(0, 16):
                    block = blockindex[world[chunk][subchunk][block]]
                    image = pygame.image.load(block.image)
                    screen.blit(image, ((chunk + block) * 16, subchunk * 16))
