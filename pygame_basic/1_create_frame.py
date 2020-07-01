import pygame

pygame.init() # 초기화 작업 (반드시 필요)
 
# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가 ?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit()