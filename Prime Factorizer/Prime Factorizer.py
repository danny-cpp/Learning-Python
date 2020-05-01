def factors(n):
    factorlist = []
    k = 2
    while(k<=n):
        while(n%k==0):
            factorlist.append(k)
            n //= k
        k +=1
    return factorlist
            

print(factors(8))
print(factors(13))
print(factors(25))
print(factors(100))
print(factors(81))
print(factors(27))

#This lists all the prime up to a number of choice

primes = []
for n in range(2,100):
    if len(factors(n))==1:
        primes.append(n)
        
print(primes)
