from Position import Position
from config import *
from Tetris import tetris_block

class  StackBlocks(object):
    def __init__(self) -> None:
        self.blocks = [[0 for j in range(BLOCK_W_COUNT)] for i in range(BLOCK_H_COUNT)] # 40 * 20 [y][x]
        
    def stack_on(self, position_list): # fuse (position_list = [Position,Position,Position ... ])
        for p in position_list:
            self.blocks[p.y][p.x] = 1 # 填值
    
    def eliminate(self):
        new_blocks = [] # 新的狀態
        eliminate_lines_count = 0 # 被消除的行數
        for line in self.blocks:
            if sum(line) == BLOCK_W_COUNT: # 可消除
                eliminate_lines_count += 1
            else:
                new_blocks.append(line)
        
        for i in range(eliminate_lines_count):
            new_blocks.insert(0, [0 for j in range(BLOCK_W_COUNT)]) # 補充在開頭
    
        self.blocks = new_blocks
    
    def check_collide(self,tetris:tetris_block):
        for b in tetris.blocks_pos:
            if (b.y + 1) >= BLOCK_H_COUNT:  # 高度到底了
                return True
            if self.blocks[b.y + 1][b.x] == 1:  # 往下一格也被佔用了
                return True
        return False