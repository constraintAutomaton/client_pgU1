import sys 
import unittest
sys.path.append(r'..\pgU1_client\localisation')
from mapping import mapping

class mapping_test(unittest.TestCase):
    def setUp(self):
        testMap = mapping('testMap')