scanners = []
l = [line.rstrip() for line in open("19_input.txt", "r").readlines()]
n = len(l)

s = []
i = 1
while i < len(l):
    if l[i] == "":
        scanners.append(s)
        s = []
        i += 2
    else:
        a = [int(x) for x in l[i].split(",")]
        s.append(a)
        i += 1
scanners.append(s)

# Rotation = (b1, b2, b3, first)
def apply_rotation(rotation, x):
    n = rotation[0] + rotation[1] + rotation[2]
    xx = [y for y in x]
    for i in range(3):
        if rotation[i]:
            xx[i] = -x[i]
    xxx = []
    for i in range(3):
        xxx.append(xx[(i + rotation[3]) % 3])
    if n % 2 == 1:
        (xxx[1], xxx[2]) = (xxx[2], xxx[1])
    return xxx

def all_rotations():
    r = []
    for b1 in range(2):
        for b2 in range(2):
            for b3 in range(2):
                for f in range(3):
                    r.append((b1, b2, b3, f))
    return r

x = [3, 1, 2]
r = all_rotations()

def minus(shift, y, x):
    for i in range(3):
        shift[i] = y[i] - x[i]

def equal_shifted(x, y, shift):
    for i in range(3):
        if x[i] + shift[i] != y[i]:
            return False
    return True

def find_connection(s0, s1):
    shift = [0, 0, 0]
    for x0 in s0:
        for y0 in s1:
            # Potential candidates
            minus(shift, y0, x0)
            c = 0
            missed = 0
            for x in s0:
                for y in s1:
                    c += equal_shifted(x, y, shift)
            if c >= 12:
                return (shift, c)
    return None

def find_connection_all_rotations(s0, s1):
    for r in all_rotations():
        ss1 = [apply_rotation(r, x) for x in s1]
        res = find_connection(s0, ss1)
        if res is not None:
            return (r, res)
    return None

not_captured = set(range(len(scanners)))
not_captured.remove(0)

captured = [scanners[0]]
center = [(0, 0, 0)]

i = 0
while i < len(captured):
    print("Using...", i)
    print("Remaining to be captured", len(not_captured), not_captured)
    x = captured[i]
    for j in set(not_captured):
        y = scanners[j]
        r = find_connection_all_rotations(x, y)
        if r is not None:
            print(j, "captured!")
            yy = [apply_rotation(r[0], p) for p in y]
            shift = r[1][0]
            yy = [(a - shift[0], b - shift[1], c - shift[2]) for (a, b, c) in yy]
            captured.append(yy)
            center.append(shift)
            not_captured.remove(j)
    i += 1

all_points = set()
for x in captured:
    for p in x:
        all_points.add((p[0], p[1], p[2]))

print(len(all_points))

m = 0
for x in center:
    for y in center:
        d = 0
        for i in range(3):
            d += abs(x[i] - y[i])
        m = max(m, d)

print(m)
