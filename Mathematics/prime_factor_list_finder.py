import math

class Prime:    
    def is_prime(number):
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0: 
                    return False
            return True
        return False

num=int(input("Enter a number to find the list of it's prime factors: "))
print('Here is the list :-', end = '  ')
print(1,end=', ')
factor=2
while int(factor) <= num/2:
    if num % factor == 0:
        if Prime.is_prime(factor) is True:
            print(factor,end=', ' )
    factor += 1
print(num)

input('Press ENTER to Exit')
