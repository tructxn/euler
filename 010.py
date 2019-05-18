import array
import time

def clc_time(func):
    start_time = time.time()
    func()
    endt_time =  time.time()
    print("execute time : " , endt_time - start_time)

pm_array = array.array('i', [2])

clc_sum = lambda a : sum(a)
def is_pm (n):
    for pm in pm_array:
        if (n % pm == 0):
            return
        if( pm *pm > n) :
            print(n)
            pm_array.append(n)
            return

    print(n)
    pm_array.append(n)
def list_pm():
    for number in range(3, 10, 2):
        is_pm(number)

    print(clc_sum(pm_array))

clc_time(list_pm)