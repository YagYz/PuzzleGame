import pygame
import sys

# Local
import level
import constants
import gameLogic

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Puzzle Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

level_index = 0

walls, targets, boxes, player = level.parse_level(level.LEVELS[level_index])

OFFSET_X = 380
OFFSET_Y = 180

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = 0, 0
            if event.key in (pygame.K_LEFT, pygame.K_a):
                dx = -1
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                dx = 1
            elif event.key in (pygame.K_UP, pygame.K_w):
                dy = -1
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                dy = 1
            elif event.key == pygame.K_r:
                level_index = 0
                walls, targets, boxes, player = level.parse_level(level.LEVELS[level_index])
            elif event.key == pygame.K_SPACE and gameLogic.is_level_completed(boxes, targets):
                if level_index + 1 < len(level.LEVELS):
                    level_index += 1
                    walls, targets, boxes, player = level.parse_level(level.LEVELS[level_index])
                
            if dx != 0 or dy != 0:
                player, boxes, result = gameLogic.try_move(player, boxes, walls, dx, dy)
                
    screen.fill(constants.COLOR_BG)
    
    for x, y in walls:
        item = (OFFSET_X + x * constants.TILE_SIZE, OFFSET_Y + y * constants.TILE_SIZE, constants.TILE_SIZE, constants.TILE_SIZE)
        pygame.draw.rect(screen, constants.COLOR_WALL, item)
    
    for x, y in targets:
        item = (OFFSET_X + x * constants.TILE_SIZE + 16, OFFSET_Y + y * constants.TILE_SIZE  + 16, 32, 32)
        pygame.draw.rect(screen, constants.COLOR_TARGET, item)
            
    for x, y in boxes:
        color = constants.COLOR_BOX_ON_TARGET if (x,y) in targets else constants.COLOR_BOX
        item = (OFFSET_X + x * constants.TILE_SIZE + 4, OFFSET_Y + y * constants.TILE_SIZE + 4, constants.TILE_SIZE - 8, constants.TILE_SIZE - 8)
        pygame.draw.rect(screen, color, item, border_radius=6)
        
    px, py = player
    player_rect = (OFFSET_X + px * constants.TILE_SIZE + 8, OFFSET_Y + py * constants.TILE_SIZE + 8, constants.TILE_SIZE - 16, constants.TILE_SIZE -
        16)
    pygame.draw.rect(screen, constants.COLOR_PLAYER, player_rect, border_radius=8)
    
    if gameLogic.is_level_completed(boxes, targets):
        win_text = font.render("Tebrikler! Seviye Tamamlandi (space = sonraki seviye, r = yeniden baslat)", True, constants.COLOR_TEXT)
        rect = win_text.get_rect(center=(constants.SCREEN_WIDTH//2, 80))
        screen.blit(win_text, rect)
        
    pygame.display.flip()
    clock.tick(constants.FPS)
    
pygame.quit()
sys.exit()