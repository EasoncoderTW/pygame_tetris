from Position import Position
from config import *

"""
1.  @#@@

2.  #@@ / @@#
    @       @
    
3.  #@
    @@
    
4.  @#  /  #@
     @@   @@

5.  @#@
     @

"""
# 虛構block: 描述基本功能(用來被繼承)
class tetris_block(object):
    def __init__(self,blocks_pos) -> None:
        self.blocks_pos = blocks_pos # 座標組[旋轉中心,其餘座標...]
    
    def rotate(self):# (右)旋
        center = self.blocks_pos[0] # 旋轉中心 
        new_pos = [] # 新其餘座標
        for b in self.blocks_pos[1:]: # 其餘座標
            delta = b - center
            new_b = Position(center.x - delta.y, center.y + delta.x)
            new_pos.append(new_b)
        self.blocks_pos[1:] = new_pos # 更新其餘座標
    
    def down(self):# 下降
        new_pos = []
        for b in self.blocks_pos:
            new_b = b + Position(0,1)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標
    
    def left(self):# 下降
        new_pos = []
        for b in self.blocks_pos:
            new_b = b - Position(1,0)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標
    
    def right(self):# 下降
        new_pos = []
        for b in self.blocks_pos:
            new_b = b + Position(1,0)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標