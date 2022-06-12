n = 100000000
primes = [0 for i in range(n+1)]
p = 2
while (p*p <= n):

    if (primes[p] == 0):
        for i in range(p * p, n+1, p):
            primes[i] = 1
    p += 1
prime = []
for i in range(len(primes)):
    if primes[i] == 0:
        prime.append(i)
prime.pop(0)
prime.pop(0)
for i in range(0,len(prime),100):
    print(prime[i])

    
 

