import sys 
import unittest
from PyQt5.QtTest import QTest
sys.path.append(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client')
from main import Main

class Gui_test(unittest.TestCase):
    def setUp(self):
        self.gui = Main()
        
