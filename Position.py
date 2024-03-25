# 座標 class
class Position(object):
    def __init__(self,x = 0,y = 0) -> None:
        self.x = x
        self.y = y
        
    def __add__(self,other):
        n = Position(self.x + other.x,self.y + other.y)
        return n

    def __sub__(self,other):
        n = Position(self.x - other.x,self.y - other.y)
        return n