def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return ackermann(x-1, ackermann(x, y-1))

print(ackermann(1, 5)) # 32
print(ackermann(2, 4)) # 65532
print(ackermann(3, 3)) # 65532

def a1(n):
    """Վերադարձնում է 2n, եթե n ը 0 չէ, այդ պարագյին կվերադարձնի 0"""
    return ackermann(0, n)

def a2(n):
    """Վերադարձնում է 2 ի n աստիճան"""
    return ackermann(1, n)

def a3(n):
    """ Case երով կհասնենք ackermann(1, ackermann(2, n-1) ->
     ackermann(1, ackermann(1, ackermann(1, n-2)))) 
     --> ackermann(1...., ackermann(1, ackermann(2, 1))) ->
     ackermann(1...., ackermann(1, 2)) ->
     ackermann(1...., 4)
        
    """
    return ackermann(2, n)