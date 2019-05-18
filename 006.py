n =100
sum = n*(n+1)/2
total = 0
for i in range(n+1):
    total += i*(sum-i)

print(total)