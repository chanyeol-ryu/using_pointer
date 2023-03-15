'''포인터 위 x,y좌표 추출'''
import pyautogui as pg
import keyboard

TM = 0
while TM == 0:
    if keyboard.is_pressed('F4'):
        x, y = pg.position()           # 포인터 위치 찾기 (x,y분리)
        alertbox = pg.alert(title='완료', text='x좌표:{} y좌표:{}'.format(x,y), button='OK')
        break
