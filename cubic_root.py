def improve(n, result):
    result = ((n / (result ** 2)) + (2 * result)) / 3
    return result


def cub_root(n):
    result = 1

    close_enough = False

    while not close_enough:
        result = improve(n, result)
        if abs((result ** 3) - n) < 0.00001:
            close_enough = True

    return round(result, 3)


print(cub_root(125))
