import paramiko
import os
import sys

class Client():
    """
    the client object made whit paramiko.
    It connect to the pi and send the command to it's command window via ssh
    """    
    def __init__(self,rpiScript='/home/pi/Python_project/PgU1/PgU1/CommandModule.py'):
        self.ssh = paramiko.SSHClient()
        with open(r'config.txt'
                  ,'r') as f:
            #maybe make a function to get those
            text = f.readlines()
            start = text[0].find(':')+1
            end = text[0].find(';')
            self.ip = text[0][start:end]
            
            start = text[1].find(':')+1
            end = text[1].find(';')
            self.username = text[1][start:end]
            
            start = text[2].find(':')+1
            end = text[2].find(';')
            self.password = text[2][start:end]
            
            start = text[3].find(':')+1
            end = text[3].find(';')
            self.rpiScript = text[3][start:end]             
            
    def connection(self):
        """connect to the pi"""
        
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, username=self.username, password=self.password)
        path = self.rpiScript[:self.rpiScript.rfind('/')]
        
        (self.stdin, self.stdout, self.stderr) = self.ssh.exec_command(
            'sudo python3 {}\n'.format(self.rpiScript))  
        # for some reason readlines make the program bug and there is 2 line before the program send some useful information
        self.stdout.readline()
        self.stdout.readline()
        self.stdout.readline() 
    def send_command(self, command):
        """
        send a command and prepare to send another
        """
        self.stdin.write(command + '\n')
        self.stdin.flush()
        
        data = self.stdout.readline()
        message = data[data.find(':')+2:-1]
        return message
    def change_connection_info(self,ip,username,password,rpiScript):
        """
        change the info of the config file
        """
        with open(r'config.txt','w') as f:
            text = 'ip:{};\nusername:{};\npassword:{};\nrpi_script:{};'.format(ip,username,password,rpiScript)
            f.write(text)
    def kill(self):
        """
        kill the ssh link
        """
        self.ssh.close()

 