from lib.setup import SCREEN, GAME
from pygame import (image, transform, 
  K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE,
  MOUSEMOTION)

class Sprite():
  def __init__(self, image_path, scale=(0,0), position=(0, 0)):
    self.path = image_path
    self.image = image.load(self.path)
    if scale[0] > 0:
      self.scale(*scale)
    self.x, self.y = position
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.limits = {
      "right": SCREEN.width - self.width,
      "bottom": SCREEN.height - self.height,
      "left": 0,
      "top": 0
    }
    self.speed = .5

  def blit(self):
    SCREEN.blit(self.image, self.x, self.y)

  def center(self):
    self.x = SCREEN.center[0] - self.width // 2
    self.y = SCREEN.center[1] - self.height // 2

  def scale(self, width, height):
    self.image = transform.scale(self.image, (width, height))

  def mouse_control(self, event):
    if event.type == MOUSEMOTION:
      self.x, self.y = (
        event.pos[0] - self.width // 2, 
        event.pos[1] - self.height // 2
      )

  def control(self, pressed, tick):
    if pressed[K_UP]:
      self.y -= self.speed * tick
    if pressed[K_DOWN]:
      self.y += self.speed * tick
    if pressed[K_LEFT]:
      self.x -= self.speed * tick
    if pressed[K_RIGHT]:
      self.x += self.speed * tick
    if pressed[K_SPACE]:
      self.center()
    if self.x > self.limits["right"]:
      self.x = self.limits["right"]
    if self.y > self.limits["bottom"]:
      self.y = self.limits["bottom"]
    if self.x < self.limits["left"]:
      self.x = self.limits["left"]
    if self.y < self.limits["top"]:
      self.y = self.limits["top"]
