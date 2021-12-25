l = [int(x) for x in open("7_input.txt").readlines()[0].split(",")]
n = len(l)

def old_cost(pos):
    c = 0
    for x in l:
        c += abs(x - pos)
    return c

def cost(pos):
    c = 0
    for x in l:
        n = abs(x - pos)
        c += (n * (n + 1)) / 2
    return c

# Gradient descent
a = min(l)
b = max(l)

def middle(a, b):
    return a + (b - a) // 2

while abs(b - a) >= 2:
    m = middle(a, b)
    assert m != a
    assert m != b
    if cost(m + 1) < cost(m):
        a = m
    elif cost(m - 1) < cost(m):
        b = m
    else:
        a = m
        b = m

c = min(cost(a), cost(b))
c = min(c, cost(a+1))

print(c)

