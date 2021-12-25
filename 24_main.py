import math
import random as rd

store = {}

def reset_store():
    store["w"] = 0
    store["x"] = 0
    store["y"] = 0
    store["z"] = 0

program = []
program.append("inp w")
program.append("add z w")
program.append("mod z 2")
program.append("div w 2")
program.append("add y w")
program.append("mod y 2")
program.append("div w 2")
program.append("add x w")
program.append("mod x 2")
program.append("div w 2")
program.append("mod w 2")

program = ["inp x", "mul x -1"]

program = []
program.append("inp z")
program.append("inp x")
program.append("mul z 3")
program.append("eql z x")

program = [line.rstrip() for line in open("24_input.txt.orig").readlines()]

input_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]

def random_input(n):
    return [rd.randint(1, 9) for _ in range(n)]

def iterate_list(w, z, minus1, add2, shift=False):
    x = z[-1]
    if shift:
        z = z[:-1]
    if w - minus1 != x:
        z.append(w + add2)
    return z

def compute_list(inp):
    z = [0]

    z = iterate_list(inp[0], z, 14, 8) # Unavoidable
    z = iterate_list(inp[1], z, 13, 8) # Unavoidable
    z = iterate_list(inp[2], z, 13, 3) # Unavoidable
    z = iterate_list(inp[3], z, 12, 10) # Unavoidable
    z = iterate_list(inp[4], z, -12, 8, True)
    z = iterate_list(inp[5], z, 12, 8) # Unavoidable
    z = iterate_list(inp[6], z, -2, 8, True)
    z = iterate_list(inp[7], z, -11, 5, True)
    z = iterate_list(inp[8], z, 13, 9) # Unavoidable
    z = iterate_list(inp[9], z, 14, 3) #Unavoidable
    z = iterate_list(inp[10], z, 0, 4, True)
    z = iterate_list(inp[11], z, -12, 9, True)
    z = iterate_list(inp[12], z, -13, 2, True)
    z = iterate_list(inp[13], z, -6, 7, True)

    return z

# Length of inp: 7
def solve(inp):

    sol = 0

    z = [0]

    z = iterate_list(inp[0], z, 14, 8) # Unavoidable
    sol = 10 * sol + inp[0]
    z = iterate_list(inp[1], z, 13, 8) # Unavoidable
    sol = 10 * sol + inp[1]
    z = iterate_list(inp[2], z, 13, 3) # Unavoidable
    sol = 10 * sol + inp[2]
    z = iterate_list(inp[3], z, 12, 10) # Unavoidable
    sol = 10 * sol + inp[3]

    w = z[-1] - 12
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -12, 8, True)

    z = iterate_list(inp[4], z, 12, 8) # Unavoidable
    sol = 10 * sol + inp[4]
    
    w = z[-1] - 2
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -2, 8, True)

    w = z[-1] - 11
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -11, 5, True)

    z = iterate_list(inp[5], z, 13, 9) # Unavoidable
    sol = 10 * sol + inp[5]
    z = iterate_list(inp[6], z, 14, 3) # Unavoidable
    sol = 10 * sol + inp[6]

    w = z[-1]
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, 0, 4, True)

    w = z[-1] - 12
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -12, 9, True)

    w = z[-1] - 13
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -13, 2, True)

    w = z[-1] - 6
    if not (1 <= w <= 9):
        return None
    sol = 10 * sol + w
    z = iterate_list(w, z, -6, 7, True)

    return sol



def convert(z):
    c = 0
    for x in z:
        c *= 26
        c += x
    return c

def iterate(w, z, minus1, add2, shift=False):
    x = z % 26
    if shift:
        z = z // 26
    if w - minus1 != x:
        z *= 26
        z += w + add2
    return z




# True removes the last one

def compute0(inp):
    z = 0

    z = iterate(inp[0], z, 14, 8)
    z = iterate(inp[1], z, 13, 8)
    z = iterate(inp[2], z, 13, 3)
    z = iterate(inp[3], z, 12, 10)
    z = iterate(inp[4], z, -12, 8, True)
    z = iterate(inp[5], z, 12, 8)
    z = iterate(inp[6], z, -2, 8, True)
    z = iterate(inp[7], z, -11, 5, True)
    z = iterate(inp[8], z, 13, 9)
    z = iterate(inp[9], z, 14, 3)
    z = iterate(inp[10], z, 0, 4, True)
    z = iterate(inp[11], z, -12, 9, True)
    z = iterate(inp[12], z, -13, 2, True)

    # Last iteration should be avoided
    # Thus, w + 6 == z % 26

    z = iterate(inp[13], z, -6, 7, True)

    return z

def find(inp):
    z = 0

    z = iterate(inp[0], z, 14, 8)
    z = iterate(inp[1], z, 13, 8)
    z = iterate(inp[2], z, 13, 3)
    z = iterate(inp[3], z, 12, 10)
    z = iterate(inp[4], z, -12, 8, True)
    z = iterate(inp[5], z, 12, 8)
    z = iterate(inp[6], z, -2, 8, True)
    z = iterate(inp[7], z, -11, 5, True)
    z = iterate(inp[8], z, 13, 9)
    z = iterate(inp[9], z, 14, 3)
    z = iterate(inp[10], z, 0, 4, True)
    z = iterate(inp[11], z, -12, 9, True)


    w = (z % 26) - 13
    assert(1 <= w <= 9)

    z = iterate(w, z, -13, 2, True)

    # Thus, w + 6 == z % 26
    w = (z % 26) - 6
    # Constraint:
    assert(1 <= w <= 9)

    z = iterate(w, z, -6, 7, True)

    return z

def compare(inp):
    print(compute0(inp))
    print(find(inp))


def compute(program, inp, z=0):
    reset_store()
    store["z"] = z
    i = 0
    for line in program:
        # print("Executing", line)
        r = line.split(" ")
        if r[0] == "inp":
            store[r[1]] = inp[i]
            i += 1
        elif r[0] == "add":
            if r[2] in store:
                x = store[r[1]] + store[r[2]]
            else:
                x = store[r[1]] + int(r[2])
            store[r[1]] = x
        elif r[0] == "mul":
            if r[2] in store:
                x = store[r[1]] * store[r[2]]
            else:
                x = store[r[1]] * int(r[2])
            store[r[1]] = x
        elif r[0] == "div":
            if r[2] in store:
                x = math.floor(store[r[1]] // store[r[2]])
            else:
                x = math.floor(store[r[1]] // int(r[2]))
            store[r[1]] = int(x)
        elif r[0] == "mod":
            if r[2] in store:
                x = store[r[1]] % store[r[2]]
            else:
                x = store[r[1]] % int(r[2])
            store[r[1]] = x
        elif r[0] == "eql":
            if r[2] in store:
                x = store[r[1]] == store[r[2]]
            else:
                x = store[r[1]] == int(r[2])
            store[r[1]] = int(x)
        # print("State:", store)
    return store

def variations(default_digit, i_digit):
    inp = [default_digit for _ in range(14)]
    last = None
    for i in range(1, 10):
        inp[i_digit] = i
        z = compute(inp)["z"]
        print(i, z)
        if last is not None:
            print("Diff", z - last)
        last = z

M = 0
m = 10000000000000000000
for x1 in range(1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                for x5 in range(1, 10):
                    for x6 in range(1, 10):
                        for x7 in range(1, 10):
                            inp = [x1, x2, x3, x4, x5, x6, x7]
                            sol = solve(inp)
                            if sol is not None:
                                # print(sol)
                                M = max(m, sol)
                                m = min(m, sol)
print(m, M)
