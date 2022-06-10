def pow(base, exp):
    if base == 0:
        if(exp < 0):
            return "Cannot divide by zero"
        elif(exp == 0):
            return "undefined"
        else: return 1


    if exp > 0:
        result = 1
        while exp > 0:
            result *= base
            exp -= 1

    elif exp < 0:
        result = 1
        while exp < 0:
            result *= base
            exp += 1
        result = 1/result
    
    else: return 1

    return result


print(pow(2, -2))
