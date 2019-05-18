import numpy as np
import time
import array

sum_map = {1:1, 2:1, 3:1, 4:3, 5:1,6:6, 7:1, 8:1,9:4}
total_sum = 0
def clc_sum_dv(n):
    sum = 0
    for number in range (1,round(n/2) +1, 1):
        if n% number == 0:
            sum+= number
    sum_map[n] = sum
    return sum

def check_valid(n):
    global total_sum
    sum_value = 0
    if n in sum_map:
        sum_value = sum_map.get(n)
    else:
        sum_value = clc_sum_dv(n)

    if sum_value in sum_map:
        sum_sum_value = sum_map.get(sum_value)
    else:
        sum_sum_value = clc_sum_dv(sum_value)

    if(sum_sum_value == n) and sum_value != n:
        print("binggo : ", n, sum_value)
        total_sum += n
        return True
    return False

def clc_1():
    for i in range (1,10000, 1):
        check_valid(i)
    print(total_sum)

def clc_time(func):
    start_time = time.time()
    func()
    print("total Execute time: ",  time.time() - start_time)


clc_time(clc_1)
