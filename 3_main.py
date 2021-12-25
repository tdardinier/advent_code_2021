l = [x.rstrip() for x in open("3_input.txt").readlines()]
n = len(l[0])

gamma = []
epsilon = []

for i in range(n):
    print(i)
    c = 0
    for x in l:
        if x[i] == "0":
            c += 1
    if c > len(l) // 2:
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")

g = int("".join(gamma), 2)
e = int("".join(epsilon), 2)
print(g * e)


def most_common_in_list(l, i, default):
    n_0 = 0
    n_1 = 0
    for x in l:
        if x[i] == "0":
            n_0 += 1
        elif x[i] == "1":
            n_1 += 1
    if n_0 > n_1:
        return "0"
    elif n_1 > n_0:
        return "1"
    else:
        return default

i = 0
oxygen = [x for x in l]
while len(oxygen) > 1:
    print(i, oxygen)
    b = str(most_common_in_list(oxygen, i, 1))
    print(b)
    oxygen = [x for x in oxygen if x[i] == b]
    print(oxygen)
    i += 1

a = oxygen[0]

i = 0
oxygen = [x for x in l]
while len(oxygen) > 1:
    print(i, oxygen)
    b = str(most_common_in_list(oxygen, i, 1))
    print(b)
    oxygen = [x for x in oxygen if x[i] != b]
    print(oxygen)
    i += 1

g = int("".join(a), 2)
e = int("".join(oxygen[0]), 2)
print(g * e)


