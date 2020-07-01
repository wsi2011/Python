import keyboard 
import time
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") #2020_0601_102030
    img = ImageGrab.grab()
    img.save('img{}.png'.format(curr_time))

keyboard.add_hotkey('space',screenshot)

keyboard.wait('esc')