# This Python file uses the following encoding: utf-8
import os, sys

sys.path.append("/home/remi/Bureau/jeu_threes/tiles")
from tiles_moves import *

#Question 1.1 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def init_play():
	"""
	Retourne un plateau correspondant à une nouvelle partie
	Une nouvelle partie est un dictionnaire avec les clefs et valeurs suivantes :
	- 'n' : vaut 4
	- 'nb_cases_libres' : 16 au départ
	- ''tiles' : tableau de 4*4 cases initialisées à 0
		
	:Exemple:
	p= init_play() retourne le dictionnaire
		
	p contient le dictionnaire {
								'n' : 4
								'nombre_cases_libres' : 16
								'tiles' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
							  }
	"""
	
	
	new_game={'n' : 4, 'nombre_cases_libres' : 16, 'tiles' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
	return new_game
	
#Question 1.8 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_game_over(plateau):

	""" 
	Return True si la partie est finie et False sinon 
    """
     
     
	if get_nb_empty_rooms(plateau)==0:
		return True
	else:
		return False
        
        
#Question 1.9 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_score(plateau):

	"""
	Retourne le score total d'une partie
	"""
	
	i=0
	count_score=0
	while i<len(plateau['tiles']):
		count_score+=plateau['tiles'][i]
		i+=1
	return count_score
	
	
##########################################################################################################################################################################################################
##########################################################################################################################################################################################################


