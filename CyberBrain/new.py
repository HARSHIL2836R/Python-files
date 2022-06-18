from cyberbrain import trace

@trace
def summ():
    a = input("Enter number one: ")
    b = input("Enter number two: ")
    return a + b

if __name__ == "__main__":
    summ()