######### p023

import numpy as np
import time
import math
abd_arr = []
limit = 28123
#limit = 30
total = 0
def clc_time(func):
    start_time = time.time()
    func()
    print("total execute time :", time.time() -start_time)

def check_abd(n):
    sum_di = 0
    end = round(math.sqrt(n)) +1
    for i in range(1,end, 1):
        if n%i == 0:
            sum_di += i
            di_2 = round(n/i)
            if di_2 != i and i >1 :
                sum_di += di_2
    if(n < sum_di):
        abd_arr.append(n)

def not_sum_abd(n):
    for index, abd in enumerate(abd_arr):
        sub = n - abd
        if sub in abd_arr:
            return False
    return True

def clc_1():
    global total
    for i in range(1,limit):

        flag = not_sum_abd(i)
        if (flag):
            total += i
        check_abd(i)
        if i % 1000 == 0:
            print(i)
    print(total)

clc_time(clc_1)

#######