M = [[int(x) for x in y.rstrip()] for y in open("9_input.txt").readlines()]

n = len(M)
m = len(M[0])

def is_defined(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def neighbours(x, y):
    l = []
    l.append((x+1, y))
    l.append((x-1, y))
    l.append((x, y+1))
    l.append((x, y-1))
    return [(x, y) for (x, y) in l if is_defined(x, y)]

def is_low_point(x, y):
    b = True
    for (xx, yy) in neighbours(x, y):
        b = b and M[x][y] < M[xx][yy]
    return b

c = 0
basins = [[None for _ in range(m)] for _ in range(n)]
i = 0
for x in range(n):
    for y in range(m):
        if is_low_point(x, y):
            c += M[x][y] + 1
            basins[x][y] = i
            i += 1

print(c)

def find_basin(x, y):
    if basins[x][y] == None:
        nei = neighbours(x, y)
        mini = min([M[xx][yy] for (xx, yy) in nei])
        for (xx, yy) in nei:
            if M[xx][yy] == mini:
                basins[x][y] = find_basin(xx, yy)
    return basins[x][y]

for x in range(n):
    for y in range(m):
        if M[x][y] != 9:
            find_basin(x, y)

sizes = [0 for _ in range(i)]
for x in range(n):
    for y in range(m):
        if M[x][y] != 9:
            sizes[basins[x][y]] += 1

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
 
