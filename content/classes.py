import os
import sys
import json
import pygame
from pygame.locals import *

from constants import *
from classes import *


class Structure():

	
	def __init__(self,file):
		self.file = file
		


	def loading(self,main_window):

		
		for element in json.load(open(self.file)):
			for i in element:
				if i == "w":
					background=pygame.image.load(background_picture).convert()	#téléchargement de la plaquette d'image floors.png
					cropped_wall=background.subsurface(background_wall)			#sélection et assignation de l'image wall issue de l'image floors
					cropped_wall=pygame.transform.scale(cropped_wall,(sprite_size,sprite_size))		#transformation de l'échelle (40x40 pixels)
					main_window.blit(cropped_wall,(window_sidex,window_sidey))	#collage de l'image wall sur la fenetre principale.
				elif i == "a":
					background=pygame.image.load(background_picture).convert()
					cropped_arrival=background.subsurface(background_arrival)
					cropped_arrival=pygame.transform.scale(cropped_arrival,(sprite_size,sprite_size))
					main_window.blit(cropped_arrival,(window_sidex,window_sidey))
					arrival_x,arrival_y=window_sidex,window_sidey
				elif i == "s":
					background=pygame.image.load(background_picture).convert()
					cropped_start=background.subsurface(background_start)
					cropped_start=pygame.transform.scale(cropped_start,(sprite_size,sprite_size))
					main_window.blit(cropped_start,(window_sidex,window_sidey))
					start_x,start_y=window_sidex,window_sidey
				elif i == "O":
					background=pygame.image.load(background_picture).convert()
					cropped_field=background.subsurface(background_field)
					cropped_field=pygame.transform.scale(cropped_field,(sprite_size,sprite_size))
					main_window.blit(cropped_field,(window_sidex,window_sidey))
				window_sidex += sprite_size
				pygame.display.flip()
			window_sidex=0
			window_sidey+=sprite_size

		




