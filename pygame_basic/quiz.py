import pygame
import random
###################################################################################################
# 초기화 작업 (반드시 필요)
pygame.init() 
 
# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("DDong Avoid Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도,폰트 등)
# 배경 만들기 
background = pygame.image.load("C:\\Users\\admin\\Documents\\python_lecture\\pygame_basic\\background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/admin/Documents/python_lecture/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 캐릭터 이동 위치
to_x = 0
character_speed = 10


# 똥 만들기 
ddong = pygame.image.load("C:/Users/admin/Documents/python_lecture/pygame_basic/enemy.png")
ddong_size = ddong .get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0,screen_width - ddong_width) 
ddong_y_pos = 0 
ddong_speed = 10


# Font 정의
game_font = pygame.font.Font(None,40)

# 게임 종료 메시지
game_result = "Game Over"

running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수 설정

    # 2. 이벤트 처리 (키보드,마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
   
    # 게임 캐릭터가 게임 화면 밖으로 못 나가게 하기 
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 똥이 떨어지도록 하기
    ddong_y_pos += ddong_speed
    
    # 똥이 떨어지다가 게임 화면 높이 보다 커지면, 즉 땅에 닿으면 사라지고 다시 위에서 생성
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0,screen_width - ddong_width) 

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos 

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos 
    ddong_rect.top = ddong_y_pos 

    if character_rect.colliderect(ddong_rect):
        print('충돌')
        running = False
        
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
    

    pygame.display.update() # 게임화면을 다시 그리기

# 게임 오버 메시지 저장
msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)
# pygame 종료
pygame.quit()