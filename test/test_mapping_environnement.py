import sys 
import os
import numpy as np
sys.path.append(os.path.join('..','pgU1_client','localisation'))
from mapping import mapping
os.chdir(os.path.join('..','pgU1_client','localisation'))

testMap = mapping('testMap')
testMap.map_generation(5,10)

testMap.change_layout(testMap.wall,9,(0,0),direction='E')
testMap.save_map()

testMap.load('testMap_version_1.map')

testMap.change_layout(testMap.wall,3,(0,8),direction='S')
print(testMap)
testMap.save_map()

testMap.change_layout(testMap.wall,5,(4,9),direction='W')
testMap.change_layout(testMap.wall,10,(0,9),direction='N')
testMap.save_map()