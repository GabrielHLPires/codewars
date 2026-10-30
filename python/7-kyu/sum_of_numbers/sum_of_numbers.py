def get_sum(a,b):
    if a > b:
        return sum(range(a, b - 1, -1))
    else:
        return sum(range(a,b + 1))