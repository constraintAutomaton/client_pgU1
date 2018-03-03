"""make a map of the area in a matrix and keep the location of the robot
for that it will record the movement of the robot by getting the speed, direction and the time of the movement
the matrix will contain a 'x for the robot a '-' or a '|' for a wall or obstacle other symbol will be choose later for other item"""
import numpy as np

class mapping():
    def __init__(self,name,i_incre=1,j_incre=1):
        self.i_incre = i_incre
        self.j_incre = j_incre
        self.unit = 'mm'
        self.CurrentMap = None
        self.version = 0
        self.mapName = name
        self.i_max = None
        self.j_max = None
        
        self.wall = '|'
        self.obstacle = '#'
        self.door = 'O'
        self.robot = 'X'
        self.road ='.'
        self.unknown = '?'
    def map_generation(self,size_i,size_j):
        self.CurrentMap = np.full((size_i,size_j),self.unknown,dtype=str)
        (self.i_max,self.j_max) = self.CurrentMap.shape
    def save_map(self):
        self.version+=1
        saveText = ''
        for i in range(0,self.i_max-1):
            for j in range(0,self.j_max-1):
                saveText = saveText + str(self.CurrentMap[i,j]) + ' '
            saveText = saveText+'\n'
        saveText = saveText+ '\n#'+'\n'+'unit:{}; incrementation in i:{};; incrementation in j:{};;; size in i:{};;;; size in j:{};;;;; name:{};;;;;; version:{}'.format(self.unit,self.i_incre,self.j_incr,self.i_max,self.j_max,self.mapName,self.version)
        
        with open(r'\map_file\{}_version_{}.map'.format(self.mapName,self.version),'w') as f:
            f.write(saveText)
    def change_layout(self,element,nb,posIni,direction='O'):
        """change the caracter of the box for the user caracter"""
        (i_ini,j_ini) = posIni
        i = i_ini
        j = j_ini
        
        for el in range(0,nb):
            if i>self.i_max:
                print('out of the map in "i"')
                break
            elif j>self.j_max:
                print('out of the map in "j"')
                break                
            if direction == 'O':
                (i,j) = (i_ini,j_ini)
            elif direction =='N':
                i+=1
            elif direction =='S':
                i-=1
            elif direction =='E':
                j+=1
            elif direction=='W':
                j-=1
        self.CurrentMap[i,j]
    def load(self,file):
        with open(r'file','r') as f:
            textMap = f.read()
            deb = textMap.find('unit:')+len('unit:')
            end = textMap.find(';')
            self.unit = textMap[deb,end]
            
            deb = textMap.find('incrementation in i:') +len('incrementation in i:')
            end = textMap.find(';;')
            self.i_incre = int(textMap[deb,end])
            
            deb  = textMap.find('incrementation in j:') +len('incrementation in j:')
            end = textMap.find(';;;')
            self.j_incre = int(textMap[deb,end])
            
            deb  = textMap.find('size in i:') +len('size in i:')
            end = textMap.find(';;;;')
            self.i_max = int(textMap[deb,end])            
            
            deb  = textMap.find('size in j:') +len('size in j:')
            end = textMap.find(';;;;;')
            self.j_max = int(textMap[deb,end])
            
            deb  = textMap.find('name:') +len('name:')
            end = textMap.find(';;;;;;')
            self.mapName = textMap[deb,end]
            
            deb  = textMap.find('version:') +len('version:')
            self.version = textMap[deb:]            
            
        self.map_generation(self.i_max,self.j_max)
        i = 0
        for line in f.readlines():
            if '#' in line:
                break
            el = np.array(line.split(' '),dtype=str)
            self.CurrentMap[i,:] = el
            i+=1    
    def __repr__(self):
        return self.CurrentMap

    def __str__(self):
        return self.CurrentMap    
            
            
            