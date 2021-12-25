f = [x.rstrip().split("-") for x in open("12_input.txt").readlines()]
M = {}
for x in f:
    (a, b) = (x[0], x[1])
    if not a in M:
        M[a] = []
    if not b in M:
        M[b] = []
    M[a].append(b)
    M[b].append(a)

def find_paths(seen, current):
    if current == "end":
        return 1
    c = 0
    if current[0].islower():
        seen.add(current)
    for x in M[current]:
        if x not in seen:
            c += find_paths(set(seen), x)
    return c

print(find_paths(set(), "start"))

def find_paths2(seen, current, twice=True):
    if current == "end":
        return 1
    c = 0
    if current[0].islower():
        seen.add(current)
    for x in M[current]:
        if x not in seen:
            c += find_paths2(set(seen), x, twice)
        elif twice and x != "start" and x != "end":
            c += find_paths2(set(seen), x, False)
    return c

print(find_paths2(set(), "start"))
