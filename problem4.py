
# Naive soln
maxPal = 0
for i in range(999, 99, -1):
    for j in range(999,99, -1):
        if str(i*j) == str(i*j)[::-1]:
            if maxPal < i*j:
                maxPal = i*j

print(maxPal)

    