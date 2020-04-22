class RangeError(Exception):
    
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return self.value

raise RangeError('Range Error!')
