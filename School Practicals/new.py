l = []
x = int(input('Enter:-'))
temp = x
while x > 0:
    y = x % 10
    x = x // 10
    l.append(y**3)
if int(sum(l)) == temp:
    print("abcd")