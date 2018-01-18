import paramiko


class Client():
    """
    the client object made whit paramiko.
    It connect to the pi and send the command to it's command window via ssh
    """    
    def __init__(self, ip='192.168.2.18', username='pi', password='raspberry'
                 , pythonScript='/home/pi/Python_project/PgU1_code/CommandModule.py'):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(ip, username=username, password=password)
            
        except:
            while exit ==False:
                print
        (self.stdin, self.stdout, self.stderr) = self.ssh.exec_command(
                ' python3 {}'.format(pythonScript))
    def send_command(self, command):
        """
        send a command and prepare to send another
        """
        self.stdin.write(command + '\n')
        self.stdin.flush()
    def change_connection_info(self,ip,username,password):
        """
        change the info of the config file
        """
        with open('config.txt','w') as f:
            text = 'ip:{};\nusername:{};\npassword:{};'.format(ip,username,password)
            f.write(text)
    def kill(self):
        """
        kill the ssh link
        """
        self.ssh.close()
a = Client()
a.change_connection_info('1','b','d')