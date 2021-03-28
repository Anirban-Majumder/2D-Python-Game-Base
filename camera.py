import pygame
from abc import ABC, abstractmethod

class Camera:
	def __init__(self, player):
		self.player = player
		self.offset = pygame.math.Vector2(0, 0)
		self.offset_float = pygame.math.Vector2(0, 0)
		self.screen_width, self.screen_height = 800, 480
		self.CONST = pygame.math.Vector2(-self.screen_width / 2 + player.rect.w / 2, -self.screen_height / 2 + self.player.rect.h/2 )

	def setmethod(self, method):
		self.method = method

	def scroll(self):
		self.method.scroll()

class CamScroll(ABC):
	def __init__(self, camera,player):
		self.camera = camera
		self.player = player

	@abstractmethod
	def scroll(self):
		pass

class Follow(CamScroll):
	def __init__(self, camera, player):
		CamScroll.__init__(self, camera, player)

	def scroll(self):
		self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
		self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
		self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Border(CamScroll):
	def __init__(self, camera, player):
		CamScroll.__init__(self, camera, player)

	def scroll(self):
		self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
		self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
		self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
		self.camera.offset.x = max(self.player.left_border, self.camera.offset.x)
		self.camera.offset.x = min(self.camera.offset.x, self.player.right_border - self.camera.screen_width)
		self.camera.offset.y = max(self.player.top_border, self.camera.offset.y)
		self.camera.offset.y = min(self.camera.offset.y, self.player.bottom_border - self.camera.screen_height)

class Auto(CamScroll):
	def __init__(self,camera,player):
		CamScroll.__init__(self,camera,player)

	def scroll(self):
		self.camera.offset.x += 1


