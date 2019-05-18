####### p20

import time
import numpy as np
import array

m_map = {1: [1]}
count = 100

def get_number_value(i):
    arr_str = list(m_map[1])
    #print(arr_str)
    arr_num = array.array('i', [])
    for num_str in arr_str:
        try:
            arr_num.append(i* int(num_str))
        except Exception:
            continue
    return arr_num

def fix_arr(num_arr_input):
    num_arr = np.array(num_arr_input)
    for index in range ( len(num_arr)-1, 0, -1):
        number = int( num_arr[index])
        if (number <10):
            continue
        new_number = int(number % 10)
        add_value =  str( number)[:-1]
        # print("number ", number, " add value : ", add_value)
        num_arr[index-1] += int(add_value)
        num_arr[index] = new_number

    return num_arr
def clc_value(i):
    num_arr = fix_arr(get_number_value(i))
    str_value = ''
    for number in num_arr:
        str_value += str(number)
    return str_value

def get_sum(str_value):
    sum = 0
    for str_number in str_value:
        try:
            number = int(str_number)
            sum += number
        except Exception:
            continue
    return sum


def clc_1():
    for index in range(2, count +1, 1):
        m_map[1]  = clc_value(index)

    print(get_sum(m_map.get(1)))


def clc_time(func):
    start_time = time.time()
    func()
    print("total execute time : ", time.time()- start_time)

clc_time(clc_1)

#######