import pygame
from Tetris import *

def draw_blocks(screen,blocks:tetris_block):
    screen.fill((0,0,0))
    for b in blocks.blocks_pos:
        # 20*20
        pygame.draw.rect(screen,(255,255,255),
            [b.x * BLOCK_SIZE, b.y * BLOCK_SIZE ,BLOCK_SIZE-BLOCK_GAP,BLOCK_SIZE-BLOCK_GAP],width=1)
    pygame.display.update()
    
def main():
    # 初始化 pygame
    pygame.init()

    # 設定視窗大小 (寬800點、高600點)
    screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HITHT))

    # 更新視窗畫面
    pygame.display.update()
    
    blocks = tetris_block([Position(11,10),Position(10,10),Position(12,10),Position(10,11)])
    draw_blocks(screen,blocks)

    # 遊戲循環
    playing = True
    while playing:
        events = pygame.event.get() # 取得事件，當下可能一個都沒有，也可能出現多個
        for event in events: # 分匹處理單一事件
            if event.type == pygame.QUIT: # 如果事件代號是 QUIT
                playing = False # 結束遊戲循環

            if event.type == pygame.KEYDOWN:
                if event.dict["key"] == pygame.K_RIGHT:
                    blocks.right()
                    draw_blocks(screen,blocks)
                if event.dict["key"] == pygame.K_LEFT:
                    blocks.left()
                    draw_blocks(screen,blocks)
                if event.dict["key"] == pygame.K_DOWN:
                    blocks.down()
                    draw_blocks(screen,blocks)
                if event.dict["key"] == pygame.K_UP:
                    blocks.rotate()
                    draw_blocks(screen,blocks)
                    
        
                    
    # 結束視窗
    pygame.quit()
    
    
if __name__ == '__main__':
    main()