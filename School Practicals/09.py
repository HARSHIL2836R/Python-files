print("This is Fibonacci Sequence:- ")
F0 = 0
F1 = 1
F2 = 1
print(F0, F1, F2, sep='\n')
for F3 in range(0, 20):
    F3 = F1 + F2
    F1 = F2
    F2 = F3
    print(F3)
print('.\n.\n.')
