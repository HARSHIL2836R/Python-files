n = int(input("Enter n :- "))
noprimes = [j for i in range(2, n) for j in range(i*2, n, i)] 
primes = [x for x in range(2, n) if x not in noprimes] 
print (primes)