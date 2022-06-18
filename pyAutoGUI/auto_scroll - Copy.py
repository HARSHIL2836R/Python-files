import pyautogui as pg
import keyboard as kb

dont_stop = True

while dont_stop == True:
    if kb.is_pressed('alt+e'):
        x = -5
        while kb.is_pressed('alt+w') == False:
            def us(x):
                x -= 1
            def ds(x):
                x += 1
            kb.hook("up", on_remove = us(x))
            kb.hook("down", on_remove = ds(x))
            pg.scroll(x)
