import pygame
import os
###################################################################################################
# 초기화 작업 (반드시 필요)
pygame.init() 
 
# 화면 크기 설정
screen_width = 640  # 가로
screen_height = 480 # 세로 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도,폰트 등)
currentPath = os.path.dirname(__file__) # 현재 파일의 위치 반환
imagePath = os.path.join(currentPath,"images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(imagePath,"background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(imagePath,"stage.png"))
stageSize = stage.get_rect().size
stageHeight = stageSize[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(imagePath,"character.png"))
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
character_x_pos = (screen_width / 2 ) - (characterWidth / 2)
character_y_pos = screen_height - characterHeight - stageHeight


running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수 설정

    # 2. 이벤트 처리 (키보드,마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의
   
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stageHeight))
    screen.blit(character,(character_x_pos,character_y_pos))

    
    pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()