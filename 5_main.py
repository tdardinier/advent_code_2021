f = open("5_input.txt", "r").readlines()
l = [x.split(" -> ") for x in f]
l = [(x[0].split(","), x[1].split(",")) for x in l]
l = [x[0] + x[1] for x in l]
l = [[int(y) for y in x] for x in l]

def is_vertical_or_horizontal(line):
    return line[0] == line[2] or line[1] == line[3]

def point_covered_by_line(x, y, line):
    if x == line[0] and x == line[2]:
        if line[1] <= y <= line[3]:
            return True
        if line[3] <= y <= line[1]:
            return True
    if y == line[1] and y == line[3]:
        if line[0] <= x <= line[2]:
            return True
        if line[2] <= x <= line[0]:
            return True
    return False



max_x = 0
max_y = 0

for line in l:
    max_x = max(max_x, line[0])
    max_x = max(max_x, line[2])

    max_y = max(max_y, line[1])
    max_y = max(max_y, line[3])

marked_diagonals = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

for line in l:
    if not is_vertical_or_horizontal(line):
        d_x = 1
        n = line[2] - line[0]
        if line[0] > line[2]:
            d_x = -1
            n = -n
        d_y = 1
        if line[1] > line[3]:
            d_y = -1
        xx = line[0]
        yy = line[1]
        for i in range(n + 1):
            marked_diagonals[xx][yy] += 1
            xx += d_x
            yy += d_y

c = 0
for i in range(max_x + 1):
    print(i, max_x)
    for j in range(max_y + 1):
        cc = marked_diagonals[i][j]
        for line in l:
            if point_covered_by_line(i, j, line):
                cc += 1
        if cc >= 2:
            c += 1

print(c)
