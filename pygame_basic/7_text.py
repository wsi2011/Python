import pygame

pygame.init() # 초기화 작업 (반드시 필요)
 
# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/admin/Documents/python_lecture/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/admin/Documents/python_lecture/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height  # 화면 세로의 가장 아래

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/admin/Documents/python_lecture/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # 화면 세로의 중앙

# 폰트 정의
game_font = pygame.font.Font(None,40) # 폰트 객체 생성

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 정보 얻어오기
print(start_ticks)

# 이벤트 루프
running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수 설정

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 방향키를 누르면 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로
                to_y += character_speed
        
        if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt   

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 적과 충돌 처리
    character_rect = character.get_rect() # 캐릭터의 위치 정보 가져오기
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 하였습니다.")
        running = False


    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기 


    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #print(pygame.time.get_ticks())
    # 경과 시간을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    # 출력할 글자, 시간,True, 글자 색상
    screen.blit(timer,(10,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print('타임아웃')
        running = False

    pygame.display.update() # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# pygame 종료
pygame.quit()