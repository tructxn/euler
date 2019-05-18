import array
primitive_array = array.array('i',[2])
my_dict = {}

def check_primitive(n):
    count = 0
    private_number = 1
    for number in primitive_array:
        if(n % number == 0):
            count +=1
            private_number = number

    if count ==0:
        primitive_array.append(n)
        add_value(n,n)
        return True
    if count == 1:
        add_value(n,private_number)

    return False

def add_value(n, i):
    if( i in my_dict) :
        value  = my_dict.get(i)
        if( value < n):
            my_dict.update({i:n})
        return
    my_dict[i] = n
    print(my_dict)

for number in range(3,20,1):
    print(number)
    check_primitive(number)
print(my_dict)
total = 1
for number, value in my_dict.items():
    total *= value

print(total)

print(primitive_array)