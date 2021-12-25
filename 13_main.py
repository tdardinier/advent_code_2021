points = set()
i = 0
l = open("13_input.txt").readlines()
for pre_line in l:
    line = pre_line.rstrip()
    if line == "":
        break
    i += 1
    a = line.split(",")
    points.add((int(a[0]), int(a[1])))

instructions = []
for pre_line in l[i+1:]:
    line = pre_line.rstrip()
    a = line.split(" ")
    b = a[2].split("=")
    instructions.append((b[0], int(b[1])))

def fold(axis, n):
    s = set()
    for (x, y) in points:
        if axis == "x" and x > n:
            s.add((2 * n - x, y))
        elif axis == "y" and y > n:
            s.add((x, 2 * n - y))
        else:
            s.add((x, y))
    return s

print(len(points))
for (axis, n) in instructions:
    points = fold(axis, n)
    print(len(points))

# Print code
for y in range(6):
    s = ""
    for x in range(40):
        if (x, y) in points:
            s += "#"
        else:
            s += " "
    print(s)

