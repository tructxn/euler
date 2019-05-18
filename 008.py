# origin_st = '123456789'
origin_st = '73167176531330624919225119674426574742355349194934'
origin_st += '96983520312774506326239578318016984801869478851843'
origin_st += '85861560789112949495459501737958331952853208805511'
origin_st += '12540698747158523863050715693290963295227443043557'
origin_st += '66896648950445244523161731856403098711121722383113'
origin_st += '62229893423380308135336276614282806444486645238749'
origin_st += '30358907296290491560440772390713810515859307960866'
origin_st += '70172427121883998797908792274921901699720888093776'
origin_st += '65727333001053367881220235421809751254540594752243'
origin_st += '52584907711670556013604839586446706324415722155397'
origin_st += '53697817977846174064955149290862569321978468622482'
origin_st += '83972241375657056057490261407972968652414535100474'
origin_st += '82166370484403199890008895243450658541227588666881'
origin_st += '16427171479924442928230863465674813919123162824586'
origin_st += '17866458359124566529476545682848912883142607690042'

origin_st += '24219022671055626321111109370544217506941658960408'
origin_st += '07198403850962455444362981230987879927244284909188'
origin_st += '84580156166097919133875499200524063689912560717606'
origin_st += '05886116467109405077541002256983155200055935729725'
origin_st += '71636269561882670428252483600823257530420752963450'

import time
import array
number_array = array.array('i',[])
def convert():
    for index in range(len(origin_st)):
        number_array.append(int(origin_st[index]))

def caculate_time(func, name):
    start_time = time.time()/1000

    func()

    end_time =time.time()/1000
    print( "time execute function " + name + " : "  + str(end_time -start_time))


def get_product(start, end):
    product = 1
    for index in range(start,end,1):
        product = product* number_array[index]

    return product

def print_result(start,end):
    product = 1
    out_array  = array.array('i', [])
    for index in range(start,end,1):
        print(index)
        value = number_array[index]
        out_array.append(value)
        product = product * value

    print(out_array, product)
    return product
def caculate1():
    jum = 4
    max_start_index = 0
    max_end_index = max_start_index + jum
    end = len(origin_st) -jum

    cusor_start_index = 1
    cusor_end_index = cusor_start_index + jum ;
    while (cusor_start_index < (end +1)):
        diff_product = 1
        diff_index = cusor_start_index - max_start_index
        product_max = get_product(max_start_index, max_start_index + diff_index)
        product_cusor = get_product(cusor_start_index, cusor_start_index + diff_index)

        print("product_max : product_cusor : " , product_max , " : " , product_cusor)
        if product_max <= product_cusor :
            max_start_index = cusor_start_index
            max_end_index = cusor_end_index
        cusor_start_index += 1
        cusor_end_index += 1

        print(cusor_start_index, cusor_end_index)

    print(max_start_index, max_end_index)
    print_result(max_start_index, max_end_index)

def caculate2():
    jum = 13
    max_start_index = 0
    max_end_index = max_start_index + jum
    end = len(origin_st) -jum
    max_product = 1
    for index in range(end+1):
        product = get_product(index, index + jum)
        if(product > max_product):
            max_end_index = index + jum
            max_start_index = index
            max_product = product

    print(max_product)
    print_result(max_start_index, max_end_index)

convert()
#print(caculate_time(caculate1, "algo"))
print(caculate_time(caculate2, "pure"))


