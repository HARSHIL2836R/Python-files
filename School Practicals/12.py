string = input("Enter Something:- ")
vowels = "aeiouAEIOU"
mx = None

for m in string:
    if m not in vowels and m.isnumeric() == False:
        mx = m
        break

for i in string:

    def Check(i):
        def consonants(i):
                if i.isalpha() is True and i not in vowels:
                    return True
        if i in string and consonants(i) == True and type(i) == str:
            return True
        if type(i) == int:
            return False

    if Check(i) == True and i >= mx:
        mx = i

print(mx, 'is the largest substring of the given string having JUST the consonants.')