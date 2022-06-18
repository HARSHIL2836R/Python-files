import PySimpleGUI as Sg
from PyDictionary import PyDictionary

red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw== "

Sg.ChangeLookAndFeel('DarkGrey10')
Sg.SetOptions(border_width=0, margins=(0, 0), element_padding=(6, 6))

diction = PyDictionary()

cursors = 'hand2'

layout = [[Sg.Text("Enter the word whose meaning you want:- ",  # Part 2 - The Layout
                   font=('colonna MT', 14),
                   justification='center')],
          [Sg.InputText(key='input',
                        font=('Cherry Cream Soda', 20),
                        text_color='#FF0000',
                        justification='center')],
          [Sg.Button('Find Meaning',
                     bind_return_key=True,
                     key='butt')],
          [Sg.MLine("",
                    key='out',
                    size=(40, 20),
                    font=('EB Garamond', 18),
                    justification='center')]]

window = Sg.Window('Dictionary',
                   layout,
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=True,
                   auto_size_buttons=True,
                   grab_anywhere=True,
                   keep_on_top=True,
                   alpha_channel=0.9,
                   )
window.read()
window.moveTo(1000, 1000)

while True:
    event, value = window.read()
    window.Move(900, 0)
    window['butt'].set_cursor(cursor='hand2')
    word = str(value['input'])
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

    if event == Sg.WIN_CLOSED or event == 'Exit':
        break
