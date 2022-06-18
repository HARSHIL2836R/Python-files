import pyautogui as pg
import keyboard as kb

dont_stop = True

while dont_stop == True:
    if kb.is_pressed('alt+e'):
        x = -5
        while kb.is_pressed('alt+w') == False:
            while kb.is_pressed('up') == False and kb.is_pressed('down') == False and kb.is_pressed('alt+w') == False:
                pg.scroll(x)
            if kb.is_pressed('up'):
                x += 1
                continue
            if kb.is_pressed('down'):
                x -= 1
                continue
