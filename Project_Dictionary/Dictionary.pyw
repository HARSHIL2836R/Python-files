import PySimpleGUI as Sg
from PyDictionary import PyDictionary

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
          [Sg.Button('Do Not Auto-Close the Window',
                     key='dclose')],
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
                   location=(1000, 0),
                   resizable=True,
                   auto_close=True,
                   auto_close_duration=15,
                   element_justification='right'
                   )

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

        if event == 'dclose':
            Sg.Window("Dictionary",
                      auto_close=False)
            event, values = window.read()
        

    if event == Sg.WIN_CLOSED or event == 'Exit':
        break
