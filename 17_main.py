x_min = 20
x_max = 30
y_min = -10
y_max = -5

x_min = 128
x_max = 160
y_min = -142
y_max = -88

def iterate(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return (x, y, vx, vy)

def trajectory(vx, vy):
    (x, y) = (0, 0)
    m = 0
    b = False
    while y >= y_min and x <= x_max:
        (x, y, vx, vy) = iterate(x, y, vx, vy)
        b = b or ((x_min <= x <= x_max) and (y_min <= y <= y_max))
        m = max(m, y)
    return (b, m)

m = 0
c = 0
for vx in range(1, x_max+1):
    for vy in range(-250, 250):
        x = trajectory(vx, vy)
        if x[0]:
            c += 1
            m = max(m, x[1])
print(m)
print(c)
