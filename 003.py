import math
import time
import array
primitive_array = array.array('i', [2,3])


def is_primitive_number(n, array):
    for i in array:
        if n % i == 0 :
            return False
        if n < i* i :
            return True
    return True

def check_primitive(check_number, array):
    print("check number " + str(check_number));
    print (array)
    if not is_primitive_number(check_number, array):
        return False
    primitive_array_lengt_before = len(array);
    max_primitive_before = array[primitive_array_lengt_before-1];
    for var in range(max_primitive_before, round(math.sqrt(check_number)), 2):
        if is_primitive_number(var, array):
            array.append(var)
            print(array)
            if( check_number % var == 0) :
                return False

    return True


number = 600851475143
out_result = 0

for var in range(3, round(math.sqrt(number)),2):
    if number % var == 0:
        print(var)
        if(check_primitive(var, primitive_array)):
            print(var)

print(primitive_array)
