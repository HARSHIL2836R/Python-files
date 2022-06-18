print("FINDING THE SUM:- ")
print("1 + x + x² + ... + xⁿ")
print("[If x = 1, the sum is (n + 1)]")

x = float(input("The value of 'x':- "))
n = float(input("The value of 'n':- "))

SUM = (x**n - 1)/(x - 1)

print("The sum is:- ", SUM)
