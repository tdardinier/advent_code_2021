import itertools

l = [x.rstrip().split(" | ") for x in open("8_input.txt").readlines()]
l = [(x[0].split(" "), x[1].split(" ")) for x in l]

specials = set([2, 4, 3, 7])

c = 0
for x in l:
    for y in x[1]:
        if len(y) in specials:
            c += 1

print(c)

alphabetical = ["a", "b", "c", "d", "e", "f", "g"]
n = len(alphabetical)

numbers = []
numbers.append("abcefg") # 0
numbers.append("cf") # 1
numbers.append("acdeg") # 2
numbers.append("acdfg") # 3
numbers.append("bcdf") # 4
numbers.append("abdfg") # 5
numbers.append("abdefg") # 6
numbers.append("acf") # 7
numbers.append("abcdefg") # 8
numbers.append("abcdfg") # 9

# numbers = [set([x for x in s]) for s in numbers]

pre_mapping = "deafgbc"
mapping = {}

for i in range(n):
    mapping[pre_mapping[i]] = alphabetical[i]

ll = l[0][0]
# ll = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")

def apply_mapping(mapping, s):
    # print(mapping, s)
    ss = [mapping[x] for x in s]
    return "".join(ss)

def is_correct(mapping, entry):
    for x in entry:
        xx = "".join(sorted(apply_mapping(mapping, x)))
        if xx not in numbers:
            return False
    return True

c = 0
for (entry, out) in l:
    print(entry, out)
    mapping = None
    for pre_m in itertools.permutations(alphabetical):
        m = {}
        for i in range(n):
            m[pre_m[i]] = alphabetical[i]
        if is_correct(m, entry):
            mapping = m
            break

    s = ""
    for y in out:
        yy = "".join(sorted(apply_mapping(mapping, y)))
        for i in range(len(numbers)):
            if yy == numbers[i]:
                s += str(i)
    print(s)
    c += int(s)

print(c)
        


