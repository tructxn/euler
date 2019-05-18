########## p022
import time
import numpy as np
import array
import string
arr = []
str_arr = ''
def init_char_arr():
    global str_arr
    str_arr = string.ascii_lowercase[:28].upper()
    print(str_arr)

def partion(arr,low,high):
    cusor = low-1
    pivot = arr[high]

    for index in range(low, high):
        if arr[index] <= pivot:
            cusor += 1
            arr[index], arr[cusor]= arr[cusor], arr[index]
    arr[cusor+1], arr[high] = arr[high], arr[cusor+1]
    return cusor+1

def s(arr,low, high):
    if low < high:
        cusor = partion(arr,low,high)
        s(arr, low, cusor-1)
        s(arr, cusor+1, high)

def sort(arr):
    s(arr,0, len(arr)-1)
    return arr

def read_input():
    f = open('./022.txt', 'r')
    arr = []
    for line in f:
        list_name = line.split(',')
    for name in list_name:
        arr.append(name.strip().replace('"', ''))
    return arr

def clc_value(name):
    total = 0
    for char in name:
        index = str_arr.find(char) +1
        total += index
    return total

def clc_1():
    arr = sort(read_input())
    init_char_arr()
    total = 0
    for index,name in enumerate(arr):
        str_value = clc_value(name) * (index+1)
        total += str_value

    print(total)

def clc_time(func):
    start_time = time.time()
    func()
    print("total execute time :", time.time() - start_time)

clc_time(clc_1)


#########