# coding: utf-8
import sys 
import os
import numpy as np
sys.path.append(os.path.join('..','pgU1_client','localisation'))
from mapping import mapping
os.chdir(os.path.join('..','pgU1_client','localisation'))


# objectif créer un carré de mur autour du domaine 
testMap = mapping('testMap') # instantiation

testMap.map_generation(5,10) # génération d'une carte (5X10)
print(testMap)
input('\n\ncontinuer')

testMap.change_layout(testMap.wall,9,(0,0),direction='E')  # trace 10 murs à l'est
testMap.save_map() # sauvegarde la carte dans un fichier versioné
print(testMap)
input('\n\ncontinuer')

testMap.load('testMap_version_1.map') # charge la carte

testMap.change_layout(testMap.wall,4,(0,9),direction='S') # trace 5 murs au sud
testMap.save_map()
print(testMap)
input('\n\ncontinuer')
testMap.load('testMap_version_2.map')

testMap.change_layout(testMap.wall,9,(4,9),direction='W') # trace 10 murs à l'ouest
testMap.save_map()
print(testMap)
input('\n\ncontinuer')

testMap.load('testMap_version_3.map')
testMap.change_layout(testMap.wall,4,(4,0),direction='N') # trace 5 murs au nord 
testMap.save_map()

print(testMap)
input('\n\ncontinuer')
print(2*'\n')

testMap.change_layout(testMap.robot,1,(1,1)) # instantiation du véhicule sur la carte en (1,1)
print(testMap)
print('\n')
input('\n\ncontinuer')
testMap.move('S',(1,1),2) # movement du véhicule au sud tout en générant des positions circulables 
#sur la carte 
print(testMap)

print('\n')
input('\n\ncontinuer')

testMap.move('E',(3,1),7) # movement du véhicule à l'est
print(testMap)

print('\n')
testMap.move('N',(3,8),2) # movement du véhicule au nord
print(testMap)

print('\n')
input('\n\ncontinuer')
testMap.move('W',(1,8),7) # movement du véhicule à l'ouest
print(testMap)
input('\n\ncontinuer')