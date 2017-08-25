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

		window_sidex=0				#MARCHE QUAND ECRIT ICI MAIS PAS QUAND DANS CONSTANTS.PY ALORS QUE LES AUTRES CONSTANTES MARCHENT ???!!!
		window_sidey=0

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




class Character():

	def __init__(self,picture,file):
		self.picture=picture
		self.file=file
		
	def loading(self,main_window):

		start_x=0
		start_y=0
		window_sidex=0
		window_sidey=0


		for element in json.load(open(self.file)):
			for i in element:
				if i == "s":
					start_x,start_y=window_sidex,window_sidey
				window_sidex+=sprite_size
			window_sidex=0
			window_sidey+=sprite_size	

		player = pygame.image.load(self.picture).convert_alpha()
		player = pygame.transform.scale(player, (player_sprite_size, player_sprite_size))
		position_player=player.get_rect(center = (start_x +20 ,start_y +20))
		main_window.blit(player,position_player)
		pygame.display.flip()


	