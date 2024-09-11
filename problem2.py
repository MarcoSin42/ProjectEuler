
f1 = 1
f2 = 2

acc = 2
while (f2 < 4_000_000):
    f2 = f1 + f2
    f1 = f2 - f1

    if f2 % 2 == 0:
        acc += f2

print(acc)
