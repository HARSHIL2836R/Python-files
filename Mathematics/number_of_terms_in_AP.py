#h is the first term of A.P.
a=int(input("Enter the first term of A.P.: "))
d=int(input("Enter the common difference of A.P.: "))
l=int(input("Enter the (term just after)last term of A.P.: "))

while a <=l:#last term
    print("The number of terms in the given AP is: ")
    print(int((l-a+d)/d))
    break
input('press ENTER to exit')
