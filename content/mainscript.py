#!/usr/bin/python3
# -*- coding: Utf-8 -*


""" Labyrinth within Mcgyver has to find and pick up 3 objects around the map in order to defeat the guardian and leave the labyrinth.
w = wall; a = arrival; O = field; s=start"""



import os
import sys
import json
import pygame
from pygame.locals import *

from constants import *
from classes import *


pygame.init()

main_window= pygame.display.set_mode((window_side,window_side))
continuer=1

Labyrinth=Structure("labyrinthe.json")
Labyrinth.loading(main_window)
pygame.display.flip()

Mcgyver=Character("Mcgyver.png","labyrinthe.json")
Mcgyver.loading(main_window)
	

while continuer:

	pygame.time.Clock().tick(30)

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		
	

	