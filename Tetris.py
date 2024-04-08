from Position import Position
from config import *
import random

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
          
        # 修正
        all_pos_x = [p.x for p in self.blocks_pos]
        min_x = min(all_pos_x)
        if min_x < 0:
            self.blocks_pos = [Position(p.x - min_x, p.y) for p in self.blocks_pos]
        max_x = max(all_pos_x)
        if max_x >= BLOCK_W_COUNT:
            self.blocks_pos = [Position(p.x - (max_x-BLOCK_W_COUNT+1), p.y) for p in self.blocks_pos]

    def down(self):# 下降
        new_pos = []
        for b in self.blocks_pos:
            new_b = b + Position(0,1)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標
    
    def left(self):# 左移
        # 判斷
        all_pos_x = [p.x for p in self.blocks_pos]
        if min(all_pos_x) == 0: #此方塊的最小x值為0 -> 這個方塊已經在最左邊了
            return # 避開不做
        new_pos = []
        for b in self.blocks_pos:
            new_b = b - Position(1,0)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標
    
    def right(self):# 右移
        # 判斷
        all_pos_x = [p.x for p in self.blocks_pos]
        if max(all_pos_x) >= BLOCK_W_COUNT-1: #此方塊的最大x值為BLOCK_W_COUNT-1 -> 這個方塊已經在最右邊了
            return # 避開不做
        new_pos = []
        for b in self.blocks_pos:
            new_b = b + Position(1,0)
            new_pos.append(new_b)
        self.blocks_pos = new_pos # 更新其餘座標
        
    def __str__(self):
        return str([(p.x, p.y) for p in self.blocks_pos])

###################################################    
# tetris generator
def tetris_generator():
    base_pos = [
        [Position(0,0), Position(-1,0), Position(1,0), Position(2,0)],
        [Position(0,0), Position(1,0), Position(2,0), Position(0,1)],
        [Position(0,0), Position(-1,0), Position(-2,0), Position(0,1)],
        [Position(0,0), Position(1,0), Position(0,1), Position(1,1)],
        [Position(0,0), Position(-1,0), Position(0,1), Position(1,1)],
        [Position(0,0), Position(1,0), Position(-1,1), Position(0,1)],
        [Position(0,0), Position(-1,0), Position(1,0), Position(0,1)],
    ]
    
    select_type = base_pos[random.randint(0,6)]
    gen_pos = [Position(p.x + BLOCK_W_COUNT//2, p.y + 2) for p in select_type]
    return tetris_block(gen_pos)
    
    
    