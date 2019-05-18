######### p024

import time

char_arr = list(range(10))
org_len = len(char_arr)

str_arr = []

def clc(str_value, arr):
    if len(str_arr) == 1000000 :
        return
    if len(arr) == org_len:
        for number in arr:
            str_value = str(number)
            new_arr = arr.copy()
            new_arr.remove(number)
            clc(str_value, new_arr)
            
    else:
        if len(arr) == 1:
            str_value += str(arr[0])
            str_arr.append(str_value)
            index = len(str_arr)
            if( index %1000 == 0):
                print(' index : ', index, ' : ', str_arr[index-1])
        else:
            for number in arr:
                len_str = org_len - len(arr)
                str_value = str_value[0: len_str]
                str_value += str(number)
                new_arr = arr.copy()
                new_arr.remove(number)
                clc(str_value, new_arr)

def clc_time(func):
    start_time = time.time()
    func()
    print('Total Execute Time : ', time.time() - start_time)


def clc_1():
    clc('', char_arr)
    print(str_arr[999999])

clc_time(clc_1)


#####