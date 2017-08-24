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

continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

			
	for element in json.load(open("labyrinthe.json")):

		Labyrinth=Structure("labyrinthe.json")
		Labyrinth.loading(main_window)


	