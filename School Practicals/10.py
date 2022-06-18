st = input("input-  ")
if len(st) % 2 == 0:
    for i in range(0, len(st)//2):
        print(st[i], '                 ', st[len(st)-i-1])
else:
    for i in range(0, len(st)//2):
        print(st[i], '                 ', st[len(st)-i-1])
    print(st[int((len(st)-1)/2)], '                 ', st[int((len(st)-1)/2)])