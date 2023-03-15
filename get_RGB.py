'''포인터 위 색상좌표 추출'''
import pyautogui as pg # 마우스 제어
import keyboard
from PIL import ImageGrab # 화면 캡쳐

TM = 0
while TM == 0:
    if keyboard.is_pressed('F4'):
        screen = ImageGrab.grab()
        pix = screen.getpixel(pg.position())
        alertbox = pg.alert(title='색상좌표', text='(RGB값: {})'.format(pix), button='OK')
        break    
