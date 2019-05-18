####### p025p

import time
from functools import lru_cache


@lru_cache()
def clc_fi(n):
    if n <2 :
        return 1
    return clc_fi(n-1) + clc_fi(n-2)

def clc_time(func):
    start_time = time.time()
    func()
    print('Total execute time ', time.time() -start_time)

def clc_1():
    len_char = 1
    index = 1
    str_value = ''
    while(1):
        
        str_value = str(clc_fi(index))
        #print(index, str_value)
        len_char = len(str_value)
        #print(clc_fi.cache_info())
        
        if(len_char) > 1000:
            return
        index += 1
    print(str_value)


clc_time(clc_1)


###########