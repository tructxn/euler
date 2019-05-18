def check(n):
    count = len(str(n))
    if count == 6:
        return isNot6(n)
    return isNot5(n)

def isNot6(n):

    _1000 = str(n)[0:3]
    _0001 = (str(n)[3:6])[::-1]

    if(_1000 != _0001):
        return True
    return False

def isNot5(n):
    _1000 = str(n)[0:2]
    _0001 = str(n)[3:5][::-1]
    if(_1000 != _0001):
        return True
    return False
def getNumber():
    max = 0
    for i in range(999,101,-1):
        print (i)
        for j in range(i,101,-1):
            sum = i*j

            if(check(sum)):
                continue
            print(i,j, sum)
            if (max == 0) :
                max = sum
                continue
            if (sum > max):
                max = sum
    return max

print(getNumber())