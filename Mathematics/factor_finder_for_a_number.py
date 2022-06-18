pr = True

while pr == True:
    num=int(input('Enter a number to find its factor: '))
    print('\n')

    print('Factors:- ',1,end=' ')

    factor=2

    while factor<=num/2:
        if num % factor==0:
            print(factor,end=' ' )
        factor += 1
        
    print(num,end='\n')
    
    print('\n')
    cf = input("Want to continue? (y/n)\n")
    
    if cf == 'n' or 'N' or 'no' or 'No' or 'NO':
        pr = False
    else:
        pr = True
