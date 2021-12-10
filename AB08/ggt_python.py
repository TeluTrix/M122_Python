
a = 18
b = 99

def ggT(x, y):
    z = x % y
    if z == 0:
        return y
    return ggT(y, z)


print(ggT(a, b))

