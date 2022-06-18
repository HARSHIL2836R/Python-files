import math

result=0
val1=float(input('Enter the first value: '))
val2=float(input('Enter the second value: '))
op=input('Enter any one of the operator (+,-,*,/): ')
if op == '+':
    result= val1+val2
elif op == '-':
    if val1>val2:
        result=val1-val2
    else:
        result=val2-val1
elif op == '*':
    result=val1*val2
elif op=='/':
    if val2==0:
        print('ERROR! Division by zero is not allowed. Program terminated')
    else:
        result = val1/val2
else:
    print('Wrong input, program terminated')
print('The result is:',result)
input('press ENTER to exit')
