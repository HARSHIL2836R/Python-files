import webbrowser
import pyautogui as py
import time

webbrowser.open('https://www.google.com')
time.sleep(5)

py.write('PyAutoGUI', interval=0.1)

time.sleep(1)

py.keyDown('return')

py.keyDown('return')

time.sleep(3)

py.moveTo(300, 360)

py.click()

time.sleep(2)

py.keyDown('tab')

time.sleep(1)

py.keyDown('return')

py.keyDown('return')

