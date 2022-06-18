# Calculator version 3.0

# Title
print("\nIn this calculator only one operator separated by a blank space can be used.")

# Pre Alloted Variables
d = "÷"
m = "×"
sm = "+"
sb = "-"
eqt = "="

class Functions:
        def summation(r):
                r.remove('+')
                sn = sum(list(map(int, r)))
                print(r[0], sm, r[1], eqt, sn)
        def multiplication(r):
                r.remove('×')
                mmn = list(map(int, r))
                meq = mmn[0] * mmn[1]
                print(r[0], m, r[1], eqt, meq)
        def multiplication2(r):
                r.remove('*')
                mmn = list(map(int, r))
                meq = mmn[0] * mmn[1]
                print(r[0], m, r[1], eqt, meq)
        def subtraction(r):
                r.remove('-')
                ssbn = list(map(int, r))
                sbeq = ssbn[0] - ssbn[1]
                print(r[0], sb, r[1], eqt, sbeq)
        def division(r):
                r.remove('÷')
                ddn = list(map(int, r))
                deq = ddn[0] / ddn[1]
                print(r[0], d, r[1], eqt, deq)

def calculator():
        ml = input("\nCalculator - ")
        r = ml.split()
        if r[1] == "+":
                Functions.summation(r)
                
        elif r[1] == '×':
                Functions.multiplication(r)
        elif r[1] == '*':
                Functions.multiplication2(r)
                
        elif r[1] == '-':
                Functions.subtraction(r)
                
        elif r[1] == '÷':
                if r[2] == '0':
                        print("Try Dividing Yourself.")
                else:
                        Functions.division(r)
                        
        else:
                print("Error")

def Continue(re):
        re = input("\nWant to use calculator again ? (y / n) - ")
        if re == "y":
                return True
        if re == "n":
                return False
        else:
                print("Follow the Syntax! And Run the program Again!!")

def __init__():
        calculator()
        while Continue("y") == True:
                calculator()

# PROGRAM STARTING HERE!
__init__()
		

