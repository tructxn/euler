###### p013
import numpy as np
arr  = np.array([])
f = open('./013.txt', 'r')

sum = np.zeros(50)

def is_number(string):
    try:
        int(string)
        return True
    except Exception:
        return False
    return False


for index, line in enumerate(f):

    list_number = list(line)
    for index_h, number in enumerate(list_number):
        if not is_number(number):
            continue
        arr = np.append(arr, int(number))

arr = arr.reshape(100,50)

for i in range(50):
    sum_col = 0
    for j in range(100):
        sum_col += arr[j][i]

    sum[i] = sum_col

#(sum)
for i in range( 49, 0, -1):
    number = int(sum[i])
    if (i == 0):
        break

    value_after = round( number%10)
    sum[i] = value_after
    if(number < 10):
        continue
    add_value = int( str(number)[:-1])
    sum[i-1] = sum[i-1] + add_value

output = ''
for i in range (10):
    number = int(sum[i])
    output = output + str(number)

    if(len(output) >= 10):
        print(output)
        break

##############
