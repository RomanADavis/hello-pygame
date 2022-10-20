import pygame
from lib.colors import BLACK

class Screen():
  def __init__(self, width=640, height=480, caption="Hello Pygame"):
    self.width = width
    self.height = height
    self.center = (width // 2, height // 2)

    self.display = pygame.display.set_mode((self.width, self.height), 0, 32)
    
    self.caption = caption
    pygame.display.set_caption(self.caption)
    
    self.fill()

  def fill(self, color = BLACK):
    self.display.fill(color)

  def blit(self, image, x=0, y=0):
    self.display.blit(image, (x, y))