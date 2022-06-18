import pyautogui as pa
import time

output = 'Continue'
output = pa.confirm(text='Be ready for Typing challenge!\n Type faster than me if you can ', title='Info', buttons=['Continue', 'Cancel'])

if output == 'Continue':

        pa.hotkey('win', 's')

        time.sleep(5)

        pa.typewrite('Notepad', interval=0.5)

        time.sleep(3)

        pa.hotkey('return')

        time.sleep(3)

        pa.typewrite('This is a fast typing challenge!!!!!', interval=1)
        pa.typewrite('\n Bet if you can type faster!! \n just type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!type!', interval=0.000001)

        pa.alert("The program is finished!\n Hope you enjoyed it....", "The End", "End")

else:
        quit()
