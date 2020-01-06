# This Python file uses the following encoding: utf-8
import os, sys

#Question 1.2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_indice(plateau, indice):
	
	"""
	Return True si l'indice correspond à un indice valide de case pour le plateau
    (entre 0 et n-1)
    """
       
	if indice <= plateau['n']-1 and indice >=0: # On oublie pas de vérifier si l'indice est positif
		return True
	else:
		return False	
		
		
#Question 1.3 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_room(plateau, lig, col):

	"""
	Return True si (lig,col) est une case du plateau
    (lig et col sont des indices valides)
    """
	if check_indice(plateau, lig) and check_indice(plateau, col) : 
		return True
	else : 
		return False

#Question 1.4 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
def get_value(plateau, lig, col):

	"""
	Return la valeur de la case (lig,col) 
	retourne une erreur si lig et col ne sont pas des indices valides
	"""
    
	if not check_room(plateau, lig, col): # Si la case n'est pas valide, on retourne une erreur
		print("Erreur")
		return False
	value=lig*plateau['n']+col # Le calcul est le suivant pour obtenir la position de la case demandée
	return plateau['tiles'][value]
	
#Question 1.5 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def set_value(plateau, lig, col, val):

	"""
	Affecte la valeure val dans la case (lig,col) du plateau
	erreur si lig,col n'est pas une case valide ou si val est une valeur incorrecte (négative)
	met aussi à jour le nombre de case libres
	"""
    
	if not check_room(plateau, lig, col) or val < 0: # Si la case n'est pas valide, on retourne une erreur
		print("Erreur")
		return False
	valeur_value=plateau['tiles'][lig*plateau['n']+col] # On récupère la valeur contenue dans la case
	if valeur_value==0 and val>0: # On compare la valeur récupérée et la valeur prise en paramètre
		plateau['nombre_cases_libres']-=1 # On met à jour le nombre de cases libres dans le dictionnaire
	if valeur_value!=0 and val == 0: 
		plateau['nombre_cases_libres']+=1 
	plateau['tiles'][lig*plateau['n']+col]=val # On remplace la valeur récupérée par la valeur prise en paramètre
	
		
#Question 1.6 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_room_empty(plateau, lig, col):

	"""
	Test si une case du plateau est libre ou pas (retourne True si c'est le cas et False sinon)
	"""
	
	if not check_room(plateau,lig,col): # Si la case n'est pas valide, on retourne une erreur
		print("Erreur")
		return False
	if plateau['tiles'][lig*plateau['n']+col]==0: # On regarde si la case est vide ou non
		return True
	else :
		return False
        
######################################################################################################################################################################################################
######################################################################################################################################################################################################

   
