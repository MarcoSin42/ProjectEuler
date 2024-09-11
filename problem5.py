sieve = [True for i in range(21)]
sieve[0] = False
sieve[1] = False
for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(i*i, len(sieve), i):
            sieve[j] = False

prod = 1
for i in range(len(sieve)):
    if sieve[i]:
        prod = prod*i



