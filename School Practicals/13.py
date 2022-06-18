string = input("Enter a string:- ")
check_out = False
for i in range(0, len(string)-1):
    if string[i] == string[len(string) - i - 1]:
        pass
    else:
        check_out = True
        break
if check_out == False:
    print(string, " is palidrome.")
else:
    print(string, " is not a palidrome.")
print("String in Uppercase :- {}\nString in Lowercase:- {}".format(string.upper(),string.lower()))