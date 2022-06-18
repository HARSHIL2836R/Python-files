class Func:

    def check_perfect(i):
        """A perfect number is the one who is the sum of its natural divisors, excluding the number itself.
        """
        def check_divisor(i, m):
            if i % m == 0:
                return True

        def p_result():
            if count != i:
                print("The number is not Perfect Number.")
            if count == i:
                print("The number is Perfect Number.")

        def p_checking():
            global count
            count = 0
            for m in range(1, i):
                if check_divisor(i, m) == True:
                    count += m
            p_result()
        #Calling Function
        p_checking()

    def check_armstrong(i):
        """An armstrong number is the sum of cubes of its digits.
        """
        def a_checking():
            global Sum
            Sum = 0
            for dig in str(i):
                Sum += int(dig)**3
            a_result()

        def a_result():
            if Sum == i:
                print("The number is an armstrong number.")
            if Sum != i:
                print("The number is not an armstrong number.")
        #Calling Function
        a_checking()

    def check_palindrome(i):
        """A palindrome is a number which looks same left to right and right to left.
        """
        def pa_checking():
            global check_out
            check_out = False
            I = str(i)
            for m in range(0, len(I) // 2):
                if I[m] == I[len(I) - m - 1]:
                    pass
                else:
                    check_out = True
                    break
            #Calling Function
            pa_result()
        def pa_result():
            if check_out == True:
                print("The number is not a palindrome.")
            if check_out == False:
                print("The number is a palindrome.")
        #Calling Function
        pa_checking()

def __init__():
    num = int(input("Enter a Number:- "))
    Func.check_perfect(num)
    Func.check_armstrong(num)
    Func.check_palindrome(num)

# Initiating the Program
__init__()