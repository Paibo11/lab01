def Evkild(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return Evkild(a - b, b)
        else:
            return Evkild(a, b - a)

print(Evkild(5, 15))