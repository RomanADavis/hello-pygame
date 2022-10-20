import pygame
from lib.screen import Screen

class Game():
  def __init__(self):
    pygame.init()
    self.screen = Screen()
    self.clock = pygame.time.Clock()

  def run(self):
    from lib.sprite import Sprite

    soccer = Sprite("./images/football.png")
    butterfly = Sprite("./images/butterfly.png", (32, 32))
    butterfly.center()
    game_over = False
    while not game_over:
      tick = self.clock.tick(100)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = True
        butterfly.mouse_control(event)
      pressed = pygame.key.get_pressed()
      butterfly.control(pressed, tick)
        
      self.screen.fill()
      soccer.blit()
      butterfly.blit()
      pygame.display.update()
