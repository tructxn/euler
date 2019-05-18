###### p012.py
import numpy as np
import time
import array
p_array = array.array('i', [2])
number = 500

def clc_time(func):
    start_time = time.time()
    func()
    print("execute time: " , time.time() - start_time)


    
def clc_1():
    count = 1
    number_local =1
    while(count <= number):
        number_local += 1
        value = round((number_local*(number_local+1))/2)
        count = clc_no_of_div_t1(value)
    print(value)
    print(count)

def clc_2():
    create_p_array()
    count = 1
    index = 1
    while (count < number):
        index += 1
        value = round(index *(index +1)/2)
        count = clc_power(value)
        
    print(value)
    print(count)
    

def create_p_array ():
    index = 3
    while len(p_array) < number :
        check_p(index)
        index +=1

def check_p(index):
    for p in p_array:
        if index % p == 0:
            return
        if p*p > index:
            break
    p_array.append(index)


def clc_power(n):
    s_map = {}
    for d in p_array:
        if n % d != 0:
            continue
        p= 1
        while ((n % np.power(d, p)) == 0):
            p = p+1
        p = p -1
        s_map[d] = p

    prod = 1
    for i, k in s_map.items():
        prod = prod * (k+1)

    return prod
def clc_no_of_div_t1(n):
    #return len(list(filter(lambda x : n %x ==0, range(1, round(n/2), 1))))
    count = 2
    for i in range (2, round(n/2) + 1,1):
        if n % i == 0:
            count = count +1

    return count

#clc_time(clc_1)
clc_time(clc_2)


####

