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

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 스피드
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(imagePath,"weapon.png"))
weaponSize = weapon.get_rect().size
weaponWidth = weaponSize[0]


# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(imagePath,"balloon1.png")),
    pygame.image.load(os.path.join(imagePath,"balloon2.png")), 
    pygame.image.load(os.path.join(imagePath,"balloon3.png")), 
    pygame.image.load(os.path.join(imagePath,"balloon4.png"))    
]

# 공 크기에 따른 최소 스피드
ball_speed_y = [-18,-15,-12,-9]

# 공들
balls = []

balls.append({
    'pos_x' : 50, # 공의 x좌표
    'pos_y' : 50, # 공의 y좌표
    'img_idx' : 0,
    'to_x' : 3,
    'to_y' : -6,
    'init_speed_y' : ball_speed_y[0]
})

running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수 설정

    # 2. 이벤트 처리 (키보드,마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (characterWidth / 2) - (weaponWidth / 2)
                weapon_y_pos = character_y_pos 
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0        

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - characterWidth:
        character_x_pos = screen_width - characterWidth

    # 무기 위치 조정
    weapons = [ [w[0],w[1] - weapon_speed] for w in weapons]
    
    # 천장에 닿은 무기 없애기
    weapons = [ [w[0],w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x'] 
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val['to_x'] =  ball_val['to_x'] * -1 # 공이 화면 밖으로 넘어가면 반대방향으로 튕김

        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stageHeight - ball_height:
            ball_val['to_y'] = ball_val['init_speed_y']
        else: # 그 외의 모든 경우에는 속도를 줄여나감
            ball_val['to_y'] += 0.5 


        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))

    for weapon_x_pos,weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0,screen_height - stageHeight))
    screen.blit(character,(character_x_pos,character_y_pos))
   
    
    pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()