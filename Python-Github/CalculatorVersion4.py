# Calculator version 3.0

# Title
print("\nIn this calculator only one operator separated by a blank space can be used.")

# Pre Alloted Variables

def v():
    d = "+"
    m = "×"
    sm = "+"
    sb = "-"
    eqt = "="
    return d,m,sm,sb,eqt

d,m,sm,sb,eqt = v()

class Functions:
        def summation(r):
                r.remove('+')
                sn = map(int, r)
                ssn = list(sn)
                eq = sum(ssn)
                print(r[0], sm, r[1], eqt, eq)
        def multiplication(r):
                r.remove('×')
                mn = map(int, r)
                mmn = list(mn)
                meq = mmn[0] * mmn[1]
                print(r[0], m, r[1], eqt, meq)
        def multiplication2(r):
                r.remove('*')
                mn = map(int, r)
                mmn = list(mn)
                meq = mmn[0] * mmn[1]
                print(r[0], m, r[1], eqt, meq)
        def subtraction(r):
                r.remove('-')
                sbn = map(int, r)
                ssbn = list(sbn)
                sbeq = ssbn[0] - ssbn[1]
                print(r[0], sb, r[1], eqt, sbeq)
        def division(r):
                        r.remove('÷')
                        dn = map(int, r)
                        ddn = list(dn)
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
		

