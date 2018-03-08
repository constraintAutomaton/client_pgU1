import sys 
import os
import unittest
import numpy as np
sys.path.append(os.path.join('..','pgU1_client','localisation'))
from mapping import mapping

class mapping_test(unittest.TestCase):
    def test_save_load_map(self):
        os.chdir(os.path.join('..','pgU1_client','localisation'))
        testMap = mapping('testMap')
        testMap.map_generation(5,10)
          
        name = testMap.mapName
        version = testMap.version
        unit = testMap.unit
        i_incre = testMap.i_incre
        j_incre = testMap.j_incre
        i_max = testMap.i_max
        j_max = testMap.j_max
        curentMap = testMap.currentMap
        testMap.save_map()
        self.assertTrue(os.path.isfile(os.path.join('map_file','testMap_version_1.map')))
        
        testMap.load(os.path.join('map_file','testMap_version_1.map'))
        self.assertEqual(testMap.mapName,name)
        self.assertEqual(testMap.version,version+1)
        self.assertEqual(testMap.unit,unit)
        self.assertEqual(testMap.i_incre,i_incre)
        self.assertEqual(testMap.j_incre,j_incre)
        self.assertEqual(testMap.i_max,i_max)
        self.assertEqual(testMap.j_max,j_max)
        self.assertTrue((testMap.currentMap==curentMap).all())
        #os.remove(os.path.join('map_file','testMap_version_1.map'))
    def test_change_layout(self):
        testMap = mapping('testMap')
        testMap.map_generation(6,10)
        
        testMap.change_layout(testMap.robot,1,(1,1))
        self.assertEqual(testMap.currentMap[1,1],testMap.robot)
        
        testMap.change_layout(testMap.robot,1,(1,1),direction='N')
        self.assertEqual(testMap.currentMap[1,1],testMap.robot)
        testMap.change_layout(testMap.robot,3,(5,1),direction='N')
    
        self.assertTrue((testMap.currentMap[2:5,1]==np.full((3,1),testMap.robot,dtype=str)).all())
        
        testMap.change_layout(testMap.robot,1,(1,1),direction='S')
        self.assertEqual(testMap.currentMap[1,1],testMap.robot)
        testMap.change_layout(testMap.robot,3,(1,1),direction='S')
        self.assertTrue((testMap.currentMap[1:4,1]==np.full((3,1),testMap.robot,dtype=str)).all())
        
        testMap.change_layout(testMap.robot,1,(1,1),direction='E')
        self.assertEqual(testMap.currentMap[1,1],testMap.robot)
        testMap.change_layout(testMap.robot,3,(1,1),direction='E')
        self.assertTrue((testMap.currentMap[1,1:4]==np.full((1,3),testMap.robot,dtype=str)).all())
        
        testMap.change_layout(testMap.robot,1,(1,1),direction='W')
        self.assertEqual(testMap.currentMap[1,1],testMap.robot)
        testMap.change_layout(testMap.robot,3,(1,5),direction='W')
        self.assertTrue((testMap.currentMap[1,2:5]==np.full((1,3),testMap.robot,dtype=str)).all())        
    def test_enlarge_map(self):
        (i_test,j_test) = (5,10)
        testMap = mapping('testMap')
        testMap.map_generation(i_test,j_test)
        testMap.change_layout(testMap.robot,1,(1,1))
        
        (i_original,j_original) = (testMap.i_max,testMap.j_max)
        listEnlarge = [0,5]
        for i_up in listEnlarge:
            for i_down in listEnlarge:
                for j_left in listEnlarge:
                    for j_right in listEnlarge:
                         testMap.map_generation(i_test,j_test)
                         testMap.enlarge_map(i_up=i_up,i_down=i_down,j_left=j_left,j_right=j_right)
                         self.assertEqual(testMap.i_max,i_original+(i_up+i_down),msg='i_up:{}; i_down:{}; j_right:{}; j_left:{}; map:\n{}'.format(i_up,i_down,j_right,j_left,testMap.currentMap))
                         self.assertEqual(testMap.j_max,j_original+(j_left+j_right),msg='i_up:{}; i_down:{}; j_right:{}; j_left:{}; map:\n{}'.format(i_up,i_down,j_right,j_left,testMap.currentMap))
    def test_move(self):
        testMap = mapping('testMap')
        testMap.map_generation(6,10)
        testMap.move('S',(1,1),3)
        
        self.assertEqual(testMap.currentMap[4,1],testMap.robot)
        self.assertEqual(testMap.currentMap[1,1],testMap.road)
                         
if __name__ == '__main__':
    unittest.main()        
    
        