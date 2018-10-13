

class Dummyplug():
    def __init__(self,state):
        self.history_of_command = list()
        self.symbol()
        self.state = state
    def symbol(self):
        
        self.forward_symbol = 'f'
        self.backward_symbol = 'b'
        self.turn_left_symbol = 'tl'
        self.turn_right_symbol = 'tr'
    def forward(self):
        
        self.history_of_command.append(self.forward_symbol)
    def backward(self):
        
        self.history_of_command.append(self.backward_symbol)
    def turn_right(self):
        
        self.history_of_command.append(self.turn_right_symbol)
    def turn_left(self):
        
        self.history_of_command.append(self.turn_left_symbol)
    
        