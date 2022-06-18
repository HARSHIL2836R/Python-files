st = input("Provide Input:- ")
cu=cl=ca=cd = 0
for i in st:
    if i.isupper():
        cu += 1
    if i.islower():
        cl += 1
    if i.isalpha():
        ca += 1
    if i.isdigit():
        cd += 1
print("""Upper case letters:- %d
Lower case letters:- %d  
Alphabets:- %d
Digits:- %d""" % (cu, cl, ca, cd))