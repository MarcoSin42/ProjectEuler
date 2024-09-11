from math import sqrt,ceil

toFactor:int = 600_851_475_143
# toFactor: int = 13195
upper = ceil(sqrt(toFactor)) 

sieve = [True for i in range(upper)]

for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(i**2, len(sieve), i):
            sieve[j] = False


for i in range(len(sieve) - 1, 0, -1):
    if sieve[i] and toFactor % i == 0:
        print(i)
        break