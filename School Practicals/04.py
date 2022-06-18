num1 = eval(input("First Number:- "))
num2 = eval(input("Second Number:- "))
num3 = eval(input("Third Number:- "))

if num1 >= num2 and num1 >= num3:
    f = num1
    if num2 >= num3:
        s = num2
        t = num3
    if num3 >= num2:
        s = num3
        t = num2

if num2 >= num1 and num2 >= num3:
    f = num2
    if num1 >= num3:
        s = num1
        t = num3
    if num3 >= num1:
        s = num3
        t = num1

if num3 >= num2 and num3 >= num1:
    f = num3
    if num2 >= num1:
        s = num2
        t = num1
    if num1 >= num2:
        s = num1
        t = num2

print("Ascending Order is:- ", t, s, f , sep='\n')
        
