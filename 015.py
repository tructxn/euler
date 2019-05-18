prod_1 = 1
for j in range ( 21, 41, 1):
    prod_1 *= j

prod_2 = 1

for i in range (1, 21):
    prod_2 *=i
    print(i, end = ' ')

print(prod_1/prod_2)
