import pygame
from Tetris import *
from Position import Position
from config import *
from StackBlocks import *

def draw_blocks(screen,blocks:tetris_block = None,stack_blocks:StackBlocks = None):
    screen.fill((0,0,0))
    if blocks is not None: # 單獨下墜的方塊
        for b in blocks.blocks_pos:
            # 20*20
            pygame.draw.rect(screen,(255,255,255),
                [WINDOWS_MARGIN+b.x * BLOCK_SIZE, WINDOWS_MARGIN+b.y * BLOCK_SIZE ,BLOCK_SIZE-BLOCK_GAP,BLOCK_SIZE-BLOCK_GAP],width=1)
    if stack_blocks is not None: # 底層堆疊的方塊
        for y,line in enumerate(stack_blocks.blocks): # 取得 行數(y), 該行list
            for x,b in enumerate(line): # 取得 個數(x), 該方塊
                if b == 1: # 需要塊方塊
                    pygame.draw.rect(screen,(255,255,0),
                        [WINDOWS_MARGIN+x * BLOCK_SIZE, WINDOWS_MARGIN+y * BLOCK_SIZE ,BLOCK_SIZE-BLOCK_GAP,BLOCK_SIZE-BLOCK_GAP],width=1)
    pygame.display.update()
    
def main():
    # 初始化 pygame
    pygame.init()

    # 設定視窗大小 (寬800點、高600點)
    screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HITHT))

    # 更新視窗畫面
    pygame.display.update()
    
    blocks = tetris_generator()
    stack_blocks = StackBlocks()
    draw_blocks(screen,blocks,stack_blocks)
    
    # 設定計時器
    pygame.time.set_timer(DROP_EVENT,300) #300ms 觸發一次

    # 遊戲循環
    playing = True
    game_state = GAME_PLAY
    while playing:
        events = pygame.event.get() # 取得事件，當下可能一個都沒有，也可能出現多個
        for event in events: # 分匹處理單一事件
            if event.type == pygame.QUIT: # 如果事件代號是 QUIT
                playing = False # 結束遊戲循環

            if event.type == pygame.TEXTINPUT:
                if event.dict["text"] == "d" and game_state == GAME_PLAY:
                    blocks.right()
                if event.dict["text"] == "a" and game_state == GAME_PLAY:
                    blocks.left()
                if event.dict["text"] == "s" and game_state == GAME_PLAY:
                    blocks.down()
                if event.dict["text"] == "w" and game_state == GAME_PLAY:
                    blocks.rotate()
                if event.dict["text"] == "p":
                    game_state = GAME_PLAY if game_state == GAME_PAUSE else GAME_PAUSE
                    if game_state == GAME_PAUSE:
                        font = pygame.font.Font("D:\CODE\C_Python_Jack\pygame\Tetris\Poppins-Bold.ttf",32)
                        text = font.render('PAUSE',True, (0,0,255), (255,255,255))
                        text_Rect = text.get_rect()
                        text_Rect.center = (WINDOWS_WIDTH // 2, WINDOWS_HITHT // 2)
                        screen.blit(text,text_Rect)
                        pygame.display.update()
                if event.dict["text"] == "r":
                    blocks = tetris_generator()
                    stack_blocks = StackBlocks()
                    draw_blocks(screen,blocks,stack_blocks)
                    game_state = GAME_PLAY
                if event.dict["text"] == " " and game_state == GAME_PLAY:
                    while not stack_blocks.check_collide(blocks):
                        blocks.down()
                    
            if event.type == DROP_EVENT and game_state == GAME_PLAY:
                blocks.down()
                   
            if stack_blocks.check_collide(blocks) and game_state == GAME_PLAY:
                stack_blocks.stack_on(blocks.blocks_pos) # 堆疊上去
                blocks = tetris_generator() # 產生新的下墜方塊
            
            if game_state == GAME_PLAY:
                stack_blocks.eliminate() # 檢查並消除
                draw_blocks(screen,blocks,stack_blocks)
            
            if stack_blocks.over_stack() and game_state == GAME_PLAY:
                font = pygame.font.Font("D:\CODE\C_Python_Jack\pygame\Tetris\Poppins-Bold.ttf",32)
                text = font.render('Game Over',True, (255,0,0), (255,255,255))
                text_Rect = text.get_rect()
                text_Rect.center = (WINDOWS_WIDTH // 2, WINDOWS_HITHT // 2)
                screen.blit(text,text_Rect)
                pygame.display.update()
                game_state = GAME_STOP
                    
    # 結束視窗
    pygame.quit()
    
    
if __name__ == '__main__':
    main()