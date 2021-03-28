import pygame
from spritesheetparser import Spritesheet
from tiles import TileMap
from camera import *
from Player import Player


pygame.init()

## GAME VARIABLE
screen_width, screen_height = 800, 480
tile_size = 32

running = True
clock = pygame.time.Clock()
TARGET_FPS = 60


## INITIALIZEING EVERYTHING
bg_img = pygame.image.load('resources/bg.jpg')
bg_img = pygame.transform.scale(bg_img, (screen_width,screen_height-tile_size*0))
display = pygame.display.set_mode(((screen_width,screen_height)))

player=Player()

camera = Camera(player)
follow = Follow(camera,player)
border = Border(camera,player)
auto = Auto(camera,player)
camera.setmethod(follow)

spritesheet = Spritesheet('resources/Blockz')
map = TileMap('map.csv', spritesheet )
player.position.x, player.position.y = map.start_x, map.start_y



while running:
	dt =clock.tick(60) * .001 * TARGET_FPS 

	## PROCESS INPUT
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

			## PROCESS KEYPRESS
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.LEFT_KEY = True
			elif event.key == pygame.K_RIGHT:
				player.RIGHT_KEY = True
			elif event.key == pygame.K_UP:
				player.UP_KEY = True
			elif event.key == pygame.K_DOWN:
				player.DOWN_KEY = True

			## HANDEL CAMERA MOVEMENT	
			elif event.key == pygame.K_1:
				camera.setmethod(follow)
			elif event.key == pygame.K_2:
				camera.setmethod(auto)
			elif event.key == pygame.K_3:
				camera.setmethod(border)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.LEFT_KEY = False
			elif event.key == pygame.K_RIGHT:
				player.RIGHT_KEY = False
			elif event.key == pygame.K_UP:
				player.UP_KEY = False
			elif event.key == pygame.K_DOWN:
				player.DOWN_KEY = False

	## SPRITE UPDATE
	player.update(dt,map.tiles)
	camera.scroll()

	## DRAW SCREEN
	display.fill((0,0,0))
	#display.blit(bg_img, (0, 0))
	map.draw_map(display, camera.offset.x, camera.offset.y)
	player.draw(display, camera.offset.x, camera.offset.y)
	#pygame.draw.rect(canvas, (255, 0, 0), player.rect, 2)
	pygame.display.update()