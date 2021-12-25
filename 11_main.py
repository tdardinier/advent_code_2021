m = [[int(x) for x in y.rstrip()] for y in open("11_input.txt").readlines()]

n = len(m)

def is_defined(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def neighbours(x, y):
    l = []
    l.append((x+1, y))
    l.append((x-1, y))
    l.append((x, y+1))
    l.append((x, y-1))
    l.append((x+1, y+1))
    l.append((x+1, y-1))
    l.append((x-1, y+1))
    l.append((x-1, y-1))
    return [(x, y) for (x, y) in l if is_defined(x, y)]

def increment():
    for i in range(n):
        for j in range(n):
            m[i][j] += 1

def reset():
    for i in range(n):
        for j in range(n):
            if m[i][j] is None:
                m[i][j] = 0

def flash(x, y):
    m[x][y] = None
    for (i, j) in neighbours(x, y):
        if m[i][j] is not None:
            m[i][j] += 1

def find_flash():
    for i in range(n):
        for j in range(n):
            if m[i][j] is not None and m[i][j] >= 10:
                return (i, j)
    return None

def step():
    increment()
    stop = False
    c = 0
    while True:
        r = find_flash()
        if r is None:
            break
        flash(r[0], r[1])
        c += 1
    reset()
    return c

counter = 0
i = 0
while True:
    i += 1
    r = step()
    if r == 100:
        print(i)
        break
    counter += r
