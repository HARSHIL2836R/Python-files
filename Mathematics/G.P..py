import math as m

print("Finding the Geometric Progression:- ")

a = float(input("Please enter the first term:- "))
r = float(input("Please enter the common difference:- "))
print("Please specify the number of terms of the G.P. to be shown, otherwise first ten terms will be displayed...")
n = float(input("No. of terms(optional):- "))

print("The G.P.:- ")

N = 0

while N <= n :
    A = a*(r**(N))

    print(A)

    N += 1

input('press ENTER to exit')

