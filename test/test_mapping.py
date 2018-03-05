import sys 
import os
import unittest
import numpy as np
sys.path.append(r'..\pgU1_client\localisation')
from mapping import mapping

class mapping_test(unittest.TestCase):
    def test_save_load_map(self):
        os.chdir(r'..\pgU1_client\localisation')
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
        self.assertTrue(os.path.isfile(r'map_file\testMap_version_1.map'))
        
        testMap.load(r'map_file\testMap_version_1.map')
        self.assertEqual(testMap.mapName,name)
        self.assertEqual(testMap.version,version+1)
        self.assertEqual(testMap.unit,unit)
        self.assertEqual(testMap.i_incre,i_incre)
        self.assertEqual(testMap.j_incre,j_incre)
        self.assertEqual(testMap.i_max,i_max)
        self.assertEqual(testMap.j_max,j_max)
        self.assertTrue((testMap.currentMap==curentMap).all())
        os.remove(r'map_file\testMap_version_1.map')
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
        
        
if __name__ == '__main__':
    unittest.main()        
    
        