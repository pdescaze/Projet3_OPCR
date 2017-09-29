import os
import sys
import json
import pygame
from pygame.locals import *



from content.constants import *



class Structure():

	
	def __init__(self,file,main_window):
		self.file = file
		self.window_sidex=0
		self.window_sidex=0
		self.start_x=0
		self.start_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.ligne_number=0
		self.sprite_number=0
		self.main_window=main_window
		self.status=0
		


	def loading(self):

		
		for element in json.load(open(self.file)):
			for i in element:
				if i == "w":
					background=pygame.image.load(background_picture).convert()	#téléchargement de la plaquette d'image floors.png
					self.cropped_wall=background.subsurface(background_wall)			#sélection et assignation de l'image wall issue de l'image floors
					self.cropped_wall=pygame.transform.scale(self.cropped_wall,(sprite_size,sprite_size))		#transformation de l'échelle (40x40 pixels)
					self.main_window.blit(self.cropped_wall,(self.window_sidex,self.window_sidey))	#collage de l'image wall sur la fenetre principale.
				elif i == "a":
					background=pygame.image.load(background_picture).convert()
					self.cropped_arrival=background.subsurface(background_arrival)
					self.cropped_arrival=pygame.transform.scale(self.cropped_arrival,(sprite_size,sprite_size))
					self.main_window.blit(self.cropped_arrival,(self.window_sidex,self.window_sidey))
					self.arrival_x,self.arrival_y=self.window_sidex,self.window_sidey
				elif i == "s":
					background=pygame.image.load(background_picture).convert()
					self.cropped_start=background.subsurface(background_start)
					self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
					self.main_window.blit(self.cropped_start,(self.window_sidex,self.window_sidey))
					self.start_x,self.start_y=self.window_sidex,self.window_sidey
					
				elif i == "O":
					background=pygame.image.load(background_picture).convert()
					self.cropped_field=background.subsurface(background_field)
					self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
					self.main_window.blit(self.cropped_field,(self.window_sidex,self.window_sidey))
				self.window_sidex += sprite_size
				pygame.display.flip()
			self.window_sidex=0
			self.window_sidey+=sprite_size


	def load_field(self,sprite_number_s,ligne_number_s):

		background=pygame.image.load(background_picture).convert()
		self.cropped_field=background.subsurface(background_field)
		self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
		self.main_window.blit(self.cropped_field,(sprite_number_s * sprite_size,ligne_number_s * sprite_size))		
	

	def load_start(self,sprite_number_s,ligne_number_s):

		background=pygame.image.load(background_picture).convert()	
		self.cropped_start=background.subsurface(background_start)
		self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
		self.main_window.blit(self.cropped_start,(sprite_number_s * sprite_size,ligne_number_s * sprite_size))


	
	def load_frame(self):
		self.frame_background=pygame.image.load(background_frame).convert()
		self.frame_background=pygame.transform.scale(self.frame_background,(window_side_x - frame_side,window_side_y))
		self.main_window.blit(self.frame_background,(frame_side,0))
		self.frame = pygame.font.SysFont("monospace", 30)
		self.frame_display = self.frame.render("McGyver Escape", 1, (255,255,0))
		self.main_window.blit(self.frame_display, title_display_position)
		pygame.display.flip()


	def test_position(self,position_player,position_guardian,catch_item1,catch_item2,catch_item3):

		if position_player == position_guardian:
			if catch_item1 == False or catch_item2 == False or catch_item3 == False:
				self.status=1
			else:
				self.status=2
		else:
			pass

		return self.status

	
	def load_victory(self,victory_picture):

		self.victory_picture=pygame.image.load(victory_picture).convert()
		self.victory_picture.set_colorkey((255,255,255))
		self.victory_picture=pygame.transform.scale(self.victory_picture,(window_side_x,window_side_y))
		self.main_window.blit(self.victory_picture,(0,0))
		self.main_window.blit(self.cropped_arrival,(self.arrival_x,self.arrival_y))
		



	def load_defeat(self,defeat_picture,artwork):

		self.defeat_picture=pygame.image.load(defeat_picture).convert()
		self.defeat_picture.set_colorkey((255,255,255))
		self.defeat_picture=pygame.transform.scale(self.defeat_picture,(window_side_x,window_side_y))
		self.main_window.blit(self.defeat_picture,(0,0))

		self.pick_blood_picture=pygame.image.load(artwork).convert_alpha()
		self.blood_picture=self.pick_blood_picture.subsurface(artwork_blood)
		self.blood_picture=pygame.transform.scale(self.blood_picture,(object_sprite_size,object_sprite_size))
		self.main_window.blit(self.cropped_arrival,(self.arrival_x,self.arrival_y))
		self.main_window.blit(self.blood_picture,(self.arrival_x,self.arrival_y))
		


		