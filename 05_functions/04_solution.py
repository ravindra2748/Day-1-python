import math

def circle(r):
    area =  (r*r) * math.pi
    coc = 2 * math.pi * r
    return round(area) , round(coc)



print(circle(2))

def truncate(f, n):
    return math.trunc(f * 10**n) / 10**n

print(truncate(1.9233, 2) )# Returns 1.92
