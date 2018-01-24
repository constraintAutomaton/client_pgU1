# coding: utf-8
import sys 
import unittest
from unittest.mock import patch
sys.path.append(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client')
from client import Client
import re
class Client_test(unittest.TestCase):
    """test every function of this repository"""
    def setUp(self):
        self.client = Client()
    
    def tearDown(self):
        self.client.kill()
    def test_connection(self):
        test = None
        try:
            self.client.connection()
            test = 1
            
        except (BadHostKeyException, AuthenticationException, 
                SSHException, socket.error) as e:
            print(e)
            test = 0
            self.client.kill()
        self.assertEqual(test,1)
    def test_format_config(self):
        """test the init function if it read rigth the info of the text file config"""
        r = re.compile('[0-9]*.[0-9]*.[0-9]*.[0-9]*')
        test = 0
        
        if r.match(self.client.ip) is not None:
            test = 1
        self.assertEqual(test,1)
        self.assertEqual(type(self.client.username),str)
        self.assertEqual(type(self.client.password),str)
    def test_change_connection_info(self):
        originalFile = ''
        with open(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client\config.txt',
                          'r') as f:
            originalFile = f.read()
                
        try:
            ip = 'ipTest'
            username = 'usernameTest'
            password = 'passwordTest'
            rpiScript = 'rpiScriptTest'
            self.client.change_connection_info(ip,username,password,rpiScript)
            
            with open(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client\config.txt',
                      'r') as f:
                text = f.readlines()
                
                self.assertEqual(text[0][:len('ip:')],'ip:')
                self.assertEqual(text[0][len('ip:'):-1],ip+';')
                
                self.assertEqual(text[1][:len('username:')],'username:')
                self.assertEqual(text[1][len('username:'):-1],username+';')
                
                self.assertEqual(text[2][:len('password:')],'password:')
                self.assertEqual(text[2][len('password:'):-1],password+';')
                
                self.assertEqual(text[3][:len('rpi_script:')],'rpi_script:')
                self.assertEqual(text[3][len('rpi_script:'):],rpiScript+';')                
                
            with open(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client\config.txt',
                  'w') as f:
                f.write(originalFile)
        except:
            with open(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\pgU1_client\config.txt',
                              'w') as f:
                f.write(originalFile)            
            raise
    def test_send_command(self):
        self.client.connection()
        self.assertEqual(self.client.send_command('test'),'command receive')
            
        
if __name__ == '__main__':
    unittest.main()