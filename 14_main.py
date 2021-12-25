f = [x.rstrip() for x in open("14_input.txt").readlines()]

current = f[0]

transfos = {}
for line in f[2:]:
    a = line.split(" -> ")
    transfos[a[0]] = a[1]

def add_pair(pairs, x, y, c):
    s = x + y
    if s not in pairs:
        pairs[s] = 0
    pairs[s] += c


pairs = {}
for i in range(len(current) - 1):
    s = current[i] + current[i+1]
    add_pair(pairs, current[i], current[i+1], 1)

def result(pairs):
    letters = set()
    for x in pairs:
        letters.add(x[0])
        letters.add(x[1])

    occurences = {}
    for x in letters:
        occurences[x] = 0

    for x in pairs:
        occurences[x[0]] += pairs[x]
        occurences[x[1]] += pairs[x]

    occurences[f[0][0]] += 1
    occurences[f[0][-1]] += 1

    M = occurences[current[0]]
    m = occurences[current[0]]
    for x in occurences:
        M = max(M, occurences[x])
        m = min(m, occurences[x])

    print((M - m) // 2)

for j in range(40):
    if j == 10:
        result(pairs)
    new_pairs = {}
    for x in pairs:
        c = transfos[x]
        add_pair(new_pairs, x[0], c, pairs[x])
        add_pair(new_pairs, c, x[1], pairs[x])
    pairs = new_pairs

result(pairs)
