import math



p1x = 0
p1y = 0


p2x = 0
p2y = 0

def circleAdd(num, a, it):
    for i in range(0 ,it):
        if a == num:
            a = 0
        else:
            a += 1
    return a


print(circleAdd(4, 2, 6))







def getVel(p1x, p1y, p2x, p2y):
    x, y = 0, 0
    if p1x > p2x:
        x = p1x - p2x
    elif p1x < p2x:
        x = p2x - p1x

    if p1y > p2y:
        y = p1y - p2y
    elif p1y < p2y:
        y  = p2y - p1y

    v = math.sqrt(x*x + y*y)
    a = math.degrees(math.asin(x / v))

    if p1x > p2x:
        if p1y > p2y:
            a = 360 - a
        elif p1y < p2y:
            a = 180 + a
    elif p1x < p2x:
        if p1y > p2y:
            a = 0 + a
        elif p1y < p2y:
            a = 180 - a
    return a ,v

def dirVel(dir, vel, d = 2):
    x = math.sin(math.radians(dir)) * (vel/d)
    y = -math.cos(math.radians(dir)) * (vel/d)
    return x, y













