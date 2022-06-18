import math

program_running = True

while program_running == True:
    def out(x, y):
        print("The Remainder is ", math.fmod(x, y))
        
    def __init__():
        print('\n')
        print("This program will help you find the remainder when a number is divided by another, \n commonly referred to as modulo in Mathematics.")
        print('\n')
        x = int(input("The Divident is: "))
        print('\n')
        y = int(input("The Divisor is: "))
        print('\n')
        out(x, y)
        print('\n')

    __init__()

    confirmation = input("Want to continue ?(y/n) \n    ")

    print('\n \n')

    if confirmation == "n":

        program_running = False

        break

    else:
        continue

