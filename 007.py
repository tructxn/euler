import array
import time
p_array = array.array('i', [2,3])

def caculate_time(func, name):
    start_time = time.time()/1000

    print(func())

    end_time =time.time()/1000
    print( "time execute function " + name + " : "  + str(end_time -start_time))

def check_primitive(n):
    for number in p_array:
        if n% number == 0:
            return False

    p_array.append(n)
    return True
index =3

value = 10001
while (len(p_array) < value):
    index = index +2
    check_primitive(index)


print(p_array[value-1])


