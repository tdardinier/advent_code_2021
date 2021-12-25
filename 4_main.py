f = open("4_input.txt").readlines()

numbers = [int(x) for x in f[0].split(",")]

grids = []
i = 2

while i < len(f):
    g = []
    for _ in range(5):
        g.append([int(f[i][k*3:k*3+2]) for k in range(5)])
        i += 1

    grids.append(g)
        
    i += 1

marked = [[[False for _ in range(5)] for _ in range(5)] for _ in grids]

def is_grid_finished(marked_grid):
    for i in range(5):
        b = True
        for j in range(5):
            b = b and marked_grid[i][j]
        if b:
            return True
    for i in range(5):
        b = True
        for j in range(5):
            b = b and marked_grid[j][i]
        if b:
            return True

def mark(n):
    for g in range(len(grids)):
        for i in range(5):
            for j in range(5):
                if grids[g][i][j] == n:
                    marked[g][i][j] = True

def one_grid_finished(marked):
    for g in range(len(grids)):
        if is_grid_finished(marked[g]):
            return g
    return None

i = 0
s = None
while s is None:
    print("Marking ", numbers[i])
    mark(numbers[i])
    i += 1
    s = one_grid_finished(marked)
n = numbers[i-1]

c = 0
for i in range(5):
    for j in range(5):
        if not marked[s][i][j]:
            c += grids[s][i][j]

print(c * n)

finished_grid = [False for _ in range(len(grids))]

i = 0
while False in finished_grid:
    mark(numbers[i])
    i += 1
    for g in range(len(grids)):
        if is_grid_finished(marked[g]) and not finished_grid[g]:
            finished_grid[g] = True
            s = g
n = numbers[i-1]

c = 0
for i in range(5):
    for j in range(5):
        if not marked[s][i][j]:
            c += grids[s][i][j]

print(c * n)


