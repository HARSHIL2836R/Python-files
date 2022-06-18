def isPrime(y):
    flag = 0
    for i in range(2, int(y/2)):
        if y % i == 0:
            flag = 1
            return False
        else:
            pass
    if flag == 0:
        return True

def check_factors(x):
    while isPrime(x) == False:
        for i in range(2, int(x/2)):
            if x % i == 0:
                break
            else:
                i = 1
        print(i, end=" x ")
        x = x / i
    print(int(x))
def main():
    num = int(eval(input("Enter a number:- ")))
    print(num, " =", end=" ")
    check_factors(num)
def __init__():
    pr = True
    while pr == True:
        main()
        ch = input("\nDo you want to continue? (y/n)\n")
        if ch == "n":
            break
__init__()