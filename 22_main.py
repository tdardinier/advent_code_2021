lines = [line.rstrip() for line in open("22_input.txt").readlines()]
lines.reverse()

new_lines = []
for line in lines:
    a = line.split(" ")
    r = a[1].split(",")

    xx = r[0][2:].split("..")
    yy = r[1][2:].split("..")
    zz = r[2][2:].split("..")

    new_line = []
    new_line.append(a[0] == "on")
    new_line.append(int(xx[0]))
    new_line.append(int(xx[1]))
    new_line.append(int(yy[0]))
    new_line.append(int(yy[1]))
    new_line.append(int(zz[0]))
    new_line.append(int(zz[1]))

    new_lines.append(new_line)

lines = new_lines

steps_x = set()
steps_y = set()
steps_z = set()

for line in new_lines:
    steps_x.add(line[1])
    steps_x.add(line[2])

    steps_y.add(line[3])
    steps_y.add(line[4])

    steps_z.add(line[5])
    steps_z.add(line[6])

steps_x = sorted(list(steps_x))
steps_y = sorted(list(steps_y))
steps_z = sorted(list(steps_z))

steps_x.append(steps_x[-1])
steps_y.append(steps_y[-1])
steps_z.append(steps_z[-1])

def is_on_point(x, y, z):
    for line in lines:
        if line[1] <= x <= line[2]:
            if line[3] <= y <= line[4]:
                if line[5] <= z <= line[6]:
                    return line[0]

# First we count "inner" points only
c = 0
for ix in range(len(steps_x) - 1):
    print(ix, len(steps_x))
    ax = steps_x[ix]
    bx = steps_x[ix + 1]
    for iy in range(len(steps_y) - 1):
        ay = steps_y[iy]
        by = steps_y[iy + 1]
        for iz in range(len(steps_z) - 1):
            az = steps_z[iz]
            bz = steps_z[iz + 1]
            if bx >= ax + 2 and by >= ay + 2 and bz >= az + 2:
                if is_on_point(ax + 1, ay + 1, az + 1):
                    c += max((bx - ax - 1) * (by - ay - 1) * (bz - az - 1), 0)

            if by >= ay + 2 and bz >= az + 2:
                if is_on_point(ax, ay + 1, az + 1):
                    c += max((by - ay - 1) * (bz - az - 1), 0)
            if bx >= ax + 2 and bz >= az + 2:
                if is_on_point(ax + 1, ay, az + 1):
                    c += max((bx - ax - 1) * (bz - az - 1), 0)
            if bx >= ax + 2 and by >= ay + 2:
                if is_on_point(ax + 1, ay + 1, az):
                    c += max((bx - ax - 1) * (by - ay - 1), 0)

            if bx >= ax + 2:
                if is_on_point(ax + 1, ay, az):
                    c += (bx - ax - 1)
            if by >= ay + 2:
                if is_on_point(ax, ay + 1, az):
                    c += (by - ay - 1)
            if bz >= az + 2:
                if is_on_point(ax, ay, az + 1):
                    c += (bz - az - 1)

            if is_on_point(ax, ay, az):
                c += 1

print(c)
