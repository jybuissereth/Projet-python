# This Python file uses the following encoding: utf-8
import os, sys

sys.path.append("/home/remi/Bureau/jeu_threes/game")
sys.path.append("/home/remi/Bureau/jeu_threes/tiles")


from tiles_moves import *
from play import *
from tiles_acces import *

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def test_check_indice():
    p=init_play()
    assert check_indice(p,0)==True #return True
    assert check_indice(p,10)==False #return False
    assert check_indice(p,3)==True #return True
    assert check_indice(p,4)==False #return False
    assert check_indice(p,-1)==False #return False
    print("Test de la fonction check_indice ok")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def test_check_room():
    p=init_play()
    assert check_room(p,2,1)==True #return True
    assert check_room(p,10,2)==False #return False
    assert check_room(p,-1,3)==False #return False
    assert check_room(p,3,3)==True #return True
    print("test de la fonction check_room ok")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def test_get_value():
    p={'n':4,
              'nombre_cases_libres':16,
              'tiles':[6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]
      }
      
    assert get_value(p,0,0)==6
    assert get_value(p,2,3)==0
    assert get_value(p,1,3)==2
    assert get_value(p,3,0)==1
    #assert get_value(p,18,3)==False
    print('test de la fonction get_value ok')   

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def test_set_value():
    print('on initialise une partie à cases vides')
    p=init_play()
    print(p['tiles'])
    print('voici le nombre de cases libres :',p['nombre_cases_libres'])
    print('On ajoute les valeurs 0,1 et 2 avec la fonction set_value')

    set_value(p,0,0,1)
    set_value(p,1,2,7)
    set_value(p,2,3,6)
    print('voici la partie avec les valeurs ajoutees')
    print(p['tiles'])
    print('on verifie que le nombre de cases libres est a jour :', p['nombre_cases_libres'])
    #assert set_value(p,18,3,1)==False
    print('test de la fonction set_value ok')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def test_is_room_empty():
    p={'n':4,
         'nombre_cases_libres':6,
              'tiles':[6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0] }
        
        
    
     
     
    assert is_room_empty(p,1,0)==True #on doit avoir True
    assert is_room_empty(p,2,3)==True #on doit avoir True
    assert is_room_empty(p,3,1)==True #on doit avoir True
    assert is_room_empty(p,0,0)==False #on doit avoir False
    assert is_room_empty(p,2,2)==False #on doit avoir False
    #assert is_room_empty(p,5,2)==False
    print("test de la fonction is_room_empty ok")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def test_check_game_over():
    p={'n':4,
         'nombre_cases_libres':1,
              'tiles':[6,2,3,2,6,2,6,2,6,2,2,6,1,2,3,0] }
    assert check_game_over(p)==False #la partie n'est pas finie car il y a une case libre
    set_value(p,3,3,1) #on complète cette case libre par la valeur 1
    assert check_game_over(p)==True #la partie doit être terminée
    print('test de la fonction check_game_over ok')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def test_get_score():
    p={'n':4,
         'nombre_cases_libres':0,
              'tiles':[6,2,3,2,12,2,6,2,6,2,2,12,1,6,3,1] }
    assert get_score(p)==68 #le score du plateau est de 68
    set_value(p,0,0,0) #on enlève la case 6, le score est à présent de 62
    assert get_score(p)==62
    print("test de la fonction get_score ok")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def test_get_nb_empty_rooms():
    p={'n':4,
         'nb_cases_libres':16,
              'tiles':[6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0] }
    assert get_nb_empty_rooms(p)==6 #il y a 6 cases libres dans le plateau
    set_value(p,3,3,1) #on rajoute une valeur dans le plateau
    assert get_nb_empty_rooms(p)==5 #il doit donc rester 5 cases libres
    set_value(p,3,3,0) # on remet deux cases libres dans le plateau
    set_value(p,0,0,0)
    assert get_nb_empty_rooms(p)==7 #il doit donc y avoir 7 cases libres
    print('test de la fonction get_nb_empty_rooms ok')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
test_check_indice()
print('')
test_check_room()
print('')
test_get_value()
print('')
test_set_value()
print('')
test_is_room_empty()
print('')
test_check_game_over()
print('')
test_get_score()
print('')
test_get_nb_empty_rooms()


