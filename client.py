import paramiko

class Client():
    def __init__(self,ip='192.168.2.24',username='pi',password='raspberry',pythonScript ='/home/pi/Documents/Python_project/PgU1_code/CommandModule.py' ):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username=username , password=password)
        (self.stdin, self.stdout, self.stderr) = self.ssh.exec_command(' python3 {}'.format(pythonScript))
     
    def sendCommand(self,command):
        self.stdin.write(command+'\n')
        self.stdin.flush()
    def kill(self):
        self.ssh.close()
         



