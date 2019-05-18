import time
from functools import lru_cache
import array
start_number = 1
def caculate_number (n):
    if(n < 2):
        return 1
    return (caculate_number(n-1) + caculate_number(n-2))

@lru_cache(maxsize=51)
def caculate_caching_number(n):
    if(n < 2):
        return 1
    return (caculate_number(n-1) + caculate_number(n-2))


def caculate_time(func, t, name):
    start_time = time.time()/1000

    print(func(t))

    end_time =time.time()/1000
    print( "time execute function " + name + " : "  + str(end_time -start_time))



#caculate_time(caculate_caching_number, 40, "caculate_caching_number" )
#caculate_time(caculate_number, 40, "caculate_number" )


fibo_array = array.array('i',[1])
fibo_array.append(1)

sum_value = 2

for i in range (2,1000):
    value = fibo_array[i-1] + fibo_array[i-2]
    if( value  > 4000000):
        break

    fibo_array.append(value)
    sum_value += value

print(sum_value/2)






