lines = [line.rstrip() for line in open("22_input_test.txt").readlines()]
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

# Invariants:
# 1. strictly ordered
# 2. pairs[i][1] < pairs[i + 1][0]

def invariant(pairs):
    for i in range(len(pairs) - 1):
        assert pairs[i][1] >= pairs[i][0]
        assert pairs[i][1] < pairs[i+1][0]


def combine_pairs(pairs_to_add):
    pairs = []
    while len(pairs_to_add) > 0:
        print(len(pairs_to_add))
        (a, b) = pairs_to_add.pop()
        i = 0
        while i < len(pairs) and a > pairs[i][1]:
            i += 1
        # 2 cases
        if i >= len(pairs):
            # 1: i = len(pairs)
            pairs.append((a, b))
        else:
            # 2: a <= pairs[i][1]
            # Two new cases:
            if b < pairs[i][0]:
                # Easy case
                # We insert (a, b) at this place
                pairs = pairs[:i] + [(a, b)] + pairs[i:]
            else:
                (aa, bb) = pairs[i]
                # We know:
                # a <= bb
                # aa <= b
                # a <= b
                # aa <= bb
                if b <= bb:
                    l = sorted(list(set([a, b, aa, bb])))
                    new_pairs = [(l[0], l[0])]
                    for j in range(len(l) - 1):
                        if l[j] + 1 <= l[j  + 1] - 1:
                            new_pairs.append((l[j] + 1, l[j + 1] - 1))
                        new_pairs.append((l[j+1], l[j+1]))
                else:
                    # b > bb
                    pairs_to_add.add((bb + 1, b))
                    l = sorted(list(set([a, aa, bb])))
                    new_pairs = [(l[0], l[0])]
                    for j in range(len(l) - 1):
                        if l[j] + 1 <= l[j + 1] - 1:
                            new_pairs.append((l[j] + 1, l[j + 1] - 1))
                        new_pairs.append((l[j+1], l[j+1]))

                pairs = pairs[:i] + new_pairs + pairs[i + 1:]

    return pairs

pairs_to_add = set()
for line in new_lines:
    pairs_to_add.add((line[1], line[2]))
pairs_x = combine_pairs(pairs_to_add)

pairs_to_add = set()
for line in new_lines:
    pairs_to_add.add((line[3], line[4]))
pairs_y = combine_pairs(pairs_to_add)

pairs_to_add = set()
for line in new_lines:
    pairs_to_add.add((line[5], line[6]))
pairs_z = combine_pairs(pairs_to_add)

def is_on_point(x, y, z):
    for line in lines:
        if line[1] <= x <= line[2]:
            if line[3] <= y <= line[4]:
                if line[5] <= z <= line[6]:
                    return line[0]
c = 0
i = 0
for (x1, x2) in pairs_x:
    i += 1
    print(i, len(pairs_x))
    for (y1, y2) in pairs_y:
        for (z1, z2) in pairs_z:
            if is_on_point(x1, y1, z1):
                c += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

print(c)
