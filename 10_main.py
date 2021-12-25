l = [x.rstrip() for x in open("10_input.txt").readlines()]

pairs = []
pairs.append(("(", ")"))
pairs.append(("[", "]"))
pairs.append(("{", "}"))
pairs.append(("<", ">"))

opening = set()
closing = set()
for (x, y) in pairs:
    opening.add(x)
    closing.add(y)

def check(s):
    stack = []
    for x in s:
        if x in opening:
            stack.append(x)
        elif x in closing:
            if (stack[-1], x) in pairs:
                stack = stack[:-1]
            else:
                return (False, x, stack)
    return (True, None, stack)

scores = {}
scores[")"] = 3
scores["]"] = 57
scores["}"] = 1197
scores[">"] = 25137

scores["("] = 1
scores["["] = 2
scores["{"] = 3
scores["<"] = 4



c1 = 0
c2 = []
for s in l:
    (b, x, stack) = check(s)
    if not b:
        c1 += scores[x]
    if b:
        c = 0
        for y in reversed(stack):
            c *= 5
            c += scores[y]
        c2.append(c)

print(c1)
c2.sort()
print(c2[len(c2) // 2])
