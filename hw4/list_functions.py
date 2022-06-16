lst = [10, 20, 30, 40, 50, 60]

def contain(data, val):
    """Checks if the list contains the value."""
    i = 0
    while i < len(data):
        if data[i] == val:
            return True
        i += 1
    return False

# print(contain(lst, 1))
# print(contain(lst, 6))

def pop(data, index=None):
    """"Removes the element by index from a list and returns it."""
    if index == None:
        result = data[-1]
        data[:] = data[:-1]
        return result
    
            
    i = 0
    result_list = []
    
    while i < len(data):
        if not i == index:
            result_list.append(data[i])
        i += 1
    result = data[index]
    data[:] = result_list
    return result

print(pop(lst, 2) )
print(lst)


def remove_all(data, val):
    """Removes all of the occurances of the given value from the list"""
    i = 0
    num_of_occurances = 0
    while i < len(data):
        if data[i] == val:
            data.remove(val)
        else:
            i += 1
    return data

# lst.append(3)
# lst.append(3)
# lst.append(6)
# lst.append(3)

# print(remove_all(lst, 3))

def reverse(data):
    """Arranges the elements of the list in reverse order."""
    i = 0
    while i < len(data)/2:
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
        i += 1
    return data

# print(reverse(lst))
# lst.append(5)
# print(reverse(lst))

def min(data):
    """Returns the minimum element value of the list."""
    result = data[0]
    i = 0
    while i < len(data):
        if result > data[i]:
            result = data[i]
        i += 1
    return result


def max(data):
    """Returns the maximum element value of the list."""
    result = data[0]
    i = 0
    while i < len(data):
        if result < data[i]:
            result = data[i]
        i += 1
    return result

# print(min(lst))
# print(max(lst))