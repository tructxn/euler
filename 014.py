import numpy as np
import time

fn_map = {1:4, 2:2,3: 8, 4:3,}
max_number = 1
max_value = 1
count = 1000000
def get_xn(x):
    if x % 2 == 0:
        return int(x/2)

    return (3*x +1)


def get_fn(x):
    global max_number
    global max_value
    if x in fn_map:
        return fn_map.get(x)
    else:
        xn = get_xn(x)
        result =  ( 1  + get_fn(xn))
        fn_map[x] = result

        if (result > max_value ):
            max_value = result
            max_number = x
        return result

def clc_1():
    for i in range ( count, 0, -1):
        get_fn(i)

    print(max_number)
    print(max_value)

def clc_time(func):
    start_time = time.time()
    func()
    print("execute time : " , time.time() - start_time)

clc_time(clc_1)
