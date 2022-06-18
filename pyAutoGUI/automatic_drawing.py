import webbrowser
import pyautogui
import time

output = pyautogui.confirm(text='This program will lead you to a browser tab where it will draw a shape automatically.\n Please do not provide any input till the end of program. ', title='Conformation', buttons=['Continue', 'Cancel'])

if output == 'OK':
        webbrowser.open('https://canvas.apps.chrome/')

        time.sleep(3)

        pyautogui.keyDown('tab')

        pyautogui.keyDown('return')

        pyautogui.moveTo(300, 300)

        time.sleep(2)

        distance = 200

        while distance > 0:
                pyautogui.drag(distance, 0, duration=0.3)   # move right
                distance -= 5
                pyautogui.drag(0, distance, duration=0.3)   # move down
                pyautogui.drag(-distance, 0, duration=0.3)  # move left
                distance -= 5
                pyautogui.drag(0, -distance, duration=0.3)  # move up

        pyautogui.alert("The program is finished!\n Hope you enjoyed it....", "The End", "End")

else:
        quit()
