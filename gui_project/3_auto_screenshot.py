import time
from PIL import ImageGrab

time.sleep(5) 

for i in range(1,11):
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴 (스샷)
    img.save('imge{}.png'.format(i)) # 스샷 이미지 저장
    time.sleep(2) 