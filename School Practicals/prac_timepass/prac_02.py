print('''
            SIMPLE INTEREST CALCULATION
''')
p = int(input("Enter Princpal amount:-   "))
r = int(input("Enter Rate of interest:-   "))
t = int(input("Enter number of years:-   "))

print("The Amount at the end of %d years is:-   "%(t), round(p + p*r*t/100))