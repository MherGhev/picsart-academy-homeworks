# 1 2 3 6 11 20 37 68
# ^ ^ ^ ^ ^  ^  ^  ^
# 1 2 3 4 5  6  7  8



def func1(n):
    if(n < 3):
        return n
    else:
        return func1(n-2) + func1(n-1) + func1(n-3)

print("Recursive")
print(func1(2)) # 2
print(func1(5)) # 11

def func2(n):
    if(n < 3):
        return n

    a = 1
    b = 2
    c = 3

    n -= 3

    while(n > 0):

        tmp = a + b + c
        a = b
        b = c
        c = tmp

        n -= 1
    return c
                
print("Iterative")
print(func2(2))
print(func2(5))

def func3(n, res = 1):
    if(n < 3):
        return n

    else:
        res = func3(n-1) + func3(n-2) + func3(n-3)
        return res

print("Tail-Recursive")
print(func3(2))
print(func3(5))
