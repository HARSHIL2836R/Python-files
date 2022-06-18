import PySimpleGUI as Sg
from PyDictionary import PyDictionary

Sg.theme('DarkBlue2')

diction = PyDictionary()

cursors = 'hand2'

layout = [[Sg.Text("Enter the word whose meaning you want:- ",
                   font=('colonna MT', 14),
                   justification='center')],  # Part 2 - The Layout
          [Sg.InputText(key='input',
                        font=('Cherry Cream Soda', 20),
                        text_color='#FF0000',
                        background_color='#fff',
                        justification='center')],
          [Sg.Button('Find Meaning',
                     bind_return_key=True,
                     key='butt')],
          [Sg.MLine("",
                    key='out',
                    size=(60, 5),
                    font=('EB Garamond', 15),
                    justification='center')]]

window = Sg.Window('Dictionary', layout)

while True:
    event, value = window.read()
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
            window['out'].print(out1)
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
