import eel
import time

eel.init('web')

@eel.expose
def my_python_method(param1, param2):
    print(param1 + param2)

eel.start('main.html', mode='edge', block=False)

eel.my_javascript_function('Hello', 'World')

while True:
    eel.sleep(10)