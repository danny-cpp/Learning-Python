def reduce(current, prime_fac):
    while (current % prime_fac == 0):
        current = current/prime_fac;
    return current;

def factors(current):
    copy_of_current = current;

    # Initialize prime array factors
    factorlist = [];
    
    # prime check + dvisibility check for n. Only n needs to check to...
    # ...sqrt(n) instead all the way up to n. O(sqrt(n)) running bound
    
    # start at 2 and 3, increase with 2 steps afterward since all even...
    # ...numbers are not prime.

    if (current % 2 == 0):
        factorlist.append(2);
        current = reduce(current, 2);

    if (current % 3 == 0):
        factorlist.append(3);
        current = reduce(current, 3);

    k = 5; # Start at 5 from now on.
    while (k*k <= current):
        if (current % k == 0):
            factorlist.append(k);
            current = reduce(current, k);

    # if the list is still empty, it means the number itself is a prime
    if (len(factorlist) == 0):
        factorlist.append(copy_of_current);

    return factorlist;
            
# Test cases
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
        
print(primes);
