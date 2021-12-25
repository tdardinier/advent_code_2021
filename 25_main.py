M = [line.rstrip() for line in open("25_input.txt").readlines()]

n = len(M)
m = len(M[0])


has_moved = True

def move_east(M):
    global has_moved
    new_M = [[x for x in y] for y in M]
    for i in range(n):
        for j in range(m):
            x = M[i][j]
            if x == ">":
                next_j = (j + 1) % m
                if M[i][next_j] == ".":
                    has_moved = True
                    new_M[i][next_j] = ">"
                    new_M[i][j] = "."
    return new_M

def move_south(M):
    global has_moved
    new_M = [[x for x in y] for y in M]
    for i in range(n):
        for j in range(m):
            x = M[i][j]
            if x == "v":
                next_i = (i + 1) % n
                if M[next_i][j] == ".":
                    has_moved = True
                    new_M[next_i][j] = "v"
                    new_M[i][j] = "."
    return new_M

i = 0
while has_moved:
    has_moved = False
    M = move_east(M)
    M = move_south(M)
    i += 1
print(i)

