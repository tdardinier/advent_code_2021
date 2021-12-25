f = open("2_input.txt").readlines()
l = [(a[0], int(a[1])) for a in [x.split(" ") for x in f]]

(h, d) = (0, 0)
for (t, x) in l:
    if t == "forward":
        h = h + x
    elif t == "down":
        d = d + x
    elif t == "up":
        d = d - x
    else:
        print("Error")

print(h * d)

(h, d, a) = (0, 0, 0)
for (t, x) in l:
    if t == "forward":
        h += x
        d += a * x
    elif t == "down":
        a += x
    elif t == "up":
        a -= x
    else:
        print("Error")

print(h * d)
