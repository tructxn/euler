import time
import numpy as np
import re
import array
m_map = {}



def read_file():
    f = open('./018.txt', 'r')
    for index, line in enumerate( f):
        arr = re.split('\s+', line)
        new_arr = array.array('i', [])
        fil_to_arr(arr, new_arr)
        np_arr = np.array(new_arr)
        m_map[index] = np_arr

def fil_to_arr(arr, new_arr):
    for str_number in arr:
        try:
            number = int(str_number)
            new_arr.append(number)
        except Exception:
            continue

#read_file()

def clc_1():
    read_file()
    deep = len(m_map) -2;
    print("deep : ", deep)
    h_len = deep
    for index in range(deep, -1, -1):
        np_arr = m_map.get(index)
        print( np_arr)
        np_arr_bot = m_map.get(index+1)
        for h_index in range(index + 1):
            value = np_arr[h_index]
            mid_bot = np_arr_bot[h_index]

            right_bot = np_arr_bot[h_index+1]
            max_value = np.amax([ mid_bot, right_bot])

            value = value + max_value
            np_arr[h_index] = value

        print(np_arr)
    print(m_map.get(0))


def clc_time(func):
    start_time = time.time()
    func()
    print("total Execute time : ", time.time() -start_time)


clc_time(clc_1)
