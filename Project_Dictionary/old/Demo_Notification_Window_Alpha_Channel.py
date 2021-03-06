#!/usr/bin/env python
import sys
import time
from PyDictionary import PyDictionary

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Demonstrates a notification window that's partially transparent
# The window slowly fades-in
# Includes a small red-X button to close the window
# Base 64 encoded button is in-lined to avoid reading a file
# Free online encoder - https://www.base64-image.de/
red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="

sg.ChangeLookAndFeel('Black')
sg.SetOptions(border_width=0, margins=(0, 0))
bcolor = ('black', '#282923')

sg.SetOptions(border_width=0, margins=(0, 0))

layout = [[sg.T('Notification' + ' ' * 14),
           sg.CloseButton('', image_data=red_x, button_color=('#282923', '#282923'))],
          [sg.T('')],
          [sg.MLine('', key='out')]]

window = sg.Window('',
                   no_titlebar=True,
                   grab_anywhere=True,
                   keep_on_top=True,
                   alpha_channel=0
                   ).Layout(layout).Finalize()

# Classy fade-in
for i in range(1, 75, 2):
    window.AlphaChannel = float(i) / 100
    time.sleep(.01)

event, values = window.Read()
while True:
    event, value = window.read()
    word = 'hell'
    dictionary = PyDictionary(word)
    meaning = dictionary.getMeanings()
    print(dictionary.printMeanings())


    def result():
        global out1, out2, out3
        dic = meaning
        for key in dic.keys():
            out1 = (key.capitalize() + ':')
            window['out'].print('\n' + out1)
            for k in dic[key].keys():
                out2 = (k + ':')
                window['out'].print(out2)
                for m in dic[key][k]:
                    out3 = m
                    window['out'].print(out3)
                    # final = out1 + "\n" + out2 + "\n" + out3
                    # window['out'].print(final)


    if event == 'butt':
        result()
        event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

