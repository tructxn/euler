import time
import array
def clc_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    run_time = end_time -start_time
    print("total running time : ", run_time)


# def test():
#     a = 10
#     x = lambda a : a + 10
#     print(x(a))

clc_a = lambda b, c : 1000 -b -c
ab_condition = lambda a, b : (a*b) % 1000 == 0
c_condition = lambda c : c%3 == 2
stop_condition = lambda a,b,c : c*c == b*b + a*a
def check():
    for c in range(500,0,-1):
        if not c_condition(c):
            continue
        for b in range(c-1,1,-1):
            a = clc_a(b,c)
            if not ab_condition(a,b):
                continue
            if stop_condition(a,b,c):
                print (a*b*c)
                return


clc_time(check)