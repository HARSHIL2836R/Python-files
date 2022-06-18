import pyautogui as py
import time

py.hotkey('win', 'r')

time.sleep(3)

py.typewrite('cmd\n', interval=0.1)

time.sleep(3)

py.typewrite('pip install pyautogui\n')


