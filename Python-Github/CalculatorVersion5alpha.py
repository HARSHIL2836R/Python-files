# Calculator version 5.1 Alpha

class Variables():
        list = ["*","x","/","+","-"]

class Func:
    def If_Else_Statements():
        if r == "+":
            return str(a + b)

        if r == "-":
            return str(a - b)

        if r == "*" or r == "x":
            return str(a * b)

        if r == "/":
            print("(Dividing will result in rounding off the divison to integer!\nSo, the final result would be smaller than the exact value.)")
            return str(a // b)
            
        else:
            print("Error")
            
    def main_task(x, i):
        """

        Checking the operator with previous and latter values into account.
        And provide result of the operation.
        Variables used:-
            a = previous value 
            b = latter value
            r = operator

        """
        global a, b, r

        #Variables
        r = x[i]
        a = int(x[i-1])
        b = int(x[i+1])
        
        return Func.If_Else_Statements()

class Calculator_running:

    def if_statements():
        """
        These are the if statements used in calc()
        Go down ↓↓↓
        """
        i = el.index(w)
        Calculator_running.manipulation(i)
        Calculator_running.final_task()

    def manipulation(i):
        el.insert(i+1, Func.main_task(el, i))
        el.pop(i)
        el.remove(str(a))
        el.remove(str(b))
    
    def check_operator(ex):
        count = ex.count(w)
        while count > 0:
            if w in el:
                Calculator_running.if_statements()
                count -= 1

    def final_task():
        """
        How you want to show the output?
        """
        print("=", " ".join(el))

    def __calc__(ex): 
        global el 
        global w
        global i
        el = ex.split()
        for w in Variables.list:
            Calculator_running.check_operator(ex)

class PreRequisites:
    def get_input():
        global ex
        ex = input("Enter an Expression:- \n")
        for w in Variables.list:
            if w in ex:
                ex = ex.replace(w, ' '+ w +' ')

def __init__():
    PreRequisites.get_input()
    Calculator_running.__calc__(ex)

__init__()