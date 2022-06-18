num = eval(input("Enter the number (or any equation without variable) to be checked:\n     "))

flag = 0
divisor = 1

print("[This input goes as ", num, "(this extra line is for operational input, example:- 2**5 + 1)]\n")
Type = type(num)

if num == 1:
    print("One is nor a prime number nor a composite number, just because the ancient people didn't think about it\n\n","The good reason for 1 not being considered prime is the fundamental theorem of arithmetic, which states that every number can be written as a product of primes in exactly one way. If 1 were prime, we would lose that uniqueness. We could write 2 as 1×2, or 1×1×2, or 1594827×2. Excluding 1 from the primes smooths that out.\n\n","'''''   HISTORY   '''''", "\n\nCaldwell and Xiong start with classical Greek mathematicians. They did not consider 1 to be a number in the same way that 2, 3, 4, and so on are numbers. 1 was considered a unit, and a number was composed of multiple units.For that reason, 1 couldn’t have been prime — it wasn’t even a number.Ninth-century Arab mathematician al-Kindī wrote that it was not a number and therefore not even or odd. The view that 1 was the building block for all numbers but not a number itself lasted for centuries.\nIn 1585, Flemish mathematician Simon Stevin pointed out that when doing arithmetic in base 10, there is no difference between the digit 1 and any other digits. For all intents and purposes, 1 behaves the way any other magnitude does.Though it was not immediate, this observation eventually led mathematicians to treat 1 as a number, just like any other number.\nThrough the end of the 19th century, some impressive mathematicians considered 1 prime, and some did not. As far as I can tell, it was not a matter that caused strife; for the most popular mathematical questions, the distinction was not terribly important.Caldwell and Xiong cite G. H. Hardy as the last major mathematician to consider 1 to be prime.(He explicitly included it as a prime in the first six editions of A Course in Pure Mathematics, which were published between 1908 and 1933. He updated the definition in 1938 to make 2 the smallest prime.)\n")

if Type != int:
    print("That's not an Integer! We work with (Positive) Integers only in here.\n\nWIKIPEDIA SAYS \n A prime number is a ```natural number``` greater than 1 that is not a product of two smaller natural numbers.\n")

if Type == int:
    for i in range(2,int(num/2)):
        if (num%i==0):
            flag=1
            divisor = i
            break

    if flag == 1:
        print(num, " is a composite number \n    Since it is Divisble by " , divisor )
        print('\n')
        
    else:
        print(num," is a prime number")
        print('\n')
        
if Type == int and num < 0:
    print("Entered number is negative integer (prime is not defined for them!!), execute again!\n\nWIKIPEDIA SAYS\n A prime number is a ```natural number``` greater than 1 that is not a product of two smaller natural numbers.\n")
