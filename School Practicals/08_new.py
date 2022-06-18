num = eval(input("Enter the number (or any equation without variable) to be checked:\n     "))

flag = 0
divisor = 1
Type = type(num)
if num == 1:
    print("One is nor a prime number nor a composite number")

if Type != int:
    print("Enter an Integer!")

if Type == int:
    for i in range(2,int(num/2)):
        if (num%i==0):
            flag=1
            divisor = i
            break
    if flag == 1:
        print(num, " is a composite number \nSince it is Least Divisble by {}.".format(divisor))
    else:
        print(num," is a prime number.")

if Type == int and num < 0:
    print("Enter positive Integer!")
