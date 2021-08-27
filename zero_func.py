import math
def func(bounds,N,func,up=True):
    ok = bounds[1]
    ng = bounds[0]
    for i in range(N):
        mid = (ok+ng)/2
        if (func(mid) > 0) == up:
            ok = mid
        else:
            ng = mid
    return ok

def fx(x):
    return math.exp(x) - math.e

print(func((-1000,1000),100,fx)) 