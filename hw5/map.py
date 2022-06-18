def my_filter(func, data):
    result = [el for el in data if func(el)]
    return result

def my_map(func, data):
    result = [None] * len(data)
    result = [func(el) for el in data]
    return result

lst = [1, 2, 3, 4]

# print(my_map(lambda el: el * 2, lst))
# print(my_filter(lambda el: el % 2 == 0, lst))

def triple(data):
    return my_map(lambda el: el * 3, data)

# print(triple(lst))

def my_map3(func, data1, data2, data3):
    if not len(data1) == len(data2) == len(data3):
        raise Exception("The lengths of lists must be equal.")
    
    result = [None] * len(data1)
    for i in range(len(data1)):
        result[i] = func(data1[i], data2[i], data3[i])
    return result

def sum(a, b, c):
    return a + b + c

lst1 = [1, 1, 1, 1]
lst2 = [4, 3, 2, 1]

# print(my_map3(sum, lst, lst1, lst2))

def my_map2(func, data1, data2):
    if not len(data1) == len(data2):
        raise Exception("The lengths of lists must be equal.")

    result = [None] * len(data1)
    for i in range(len(data1)):
        result[i] = func(data1[i], data2[i])
    return result

def my_pow(base, exp):
    return base ** exp

bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(my_map2(my_pow, bases, exps))