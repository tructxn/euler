###### p016
import numpy as np
import time
index = 1
value = '1'

def clc_time(func):
    start_time = time.time()
    func()
    print(" execute time : ", time.time() - start_time)

def clc_1():
    for i in range (1,1001,1):
        mul(i)
        if(i % 10 == 0 ):
            print("value at ", i, " : " , value)

    print(value)
    clc_sum()

def clc_sum():
    arr = list(value)
    total = 0
    for number_str in arr:
        try:
            number = int(number_str)
            total += number
        except Exception:
            continue
    print(total)

def mul(i):
    global value
    arr = list(value)
    out_arr = np.array([])
    for number_str in arr:
        try:
            number = int(number_str)
            number *=2
            out_arr = np.append(out_arr, int(number))
        except Exception:
            continue

    clc_value(i,out_arr)

def clc_value(i, out_arr):
    global value
    for index in range(len(out_arr) -1, -1, -1):
        number = int( out_arr[index])
        if index == 0:
            continue

        if number < 10 :
            continue

        new_number = int(number % 10)
        add_value = int(str(number)[:-1])
        out_arr[index-1] += add_value
        out_arr[index] = new_number

    out_value = ''
    for number in out_arr:
        out_value += str(int(number))

    value = out_value

clc_time(clc_1)
########end


