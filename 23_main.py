n = 2

# Correct 7008
s0 = ".....D.D.A."
s0 += ".ABBCC.."

# Correct 9011
s1 = ".....D....."
s1 += ".ABBCCDA"

# Correct 9041
s0 = ".....D....."
s0 += "BA.BCCDA"

# Correct 12071
s0 = "...B......." + "BA.DCCDA"


# s0 = "...........BACDBCDA"

s0 = "...........DBDCBAAC"


# Example
#n = 4
#s0 = "...........BDDACCBDBBACDACA"

# Mine
n = 4
s0 = "...........DDDBDCBCBBAAAACC"

# From this: 42540
# Not right answer

# s0 = "...........BDDACCBDBBACDACA"


# s0 = "A........BDBDDACCBD.BAC..CA"
# 44169
s0 = "..........."
s0 += "DDDC"
s0 += "ACBC"
s0 += "ABAB"
s0 += "DACB"





costs = {}
costs["A"] = 1
costs["B"] = 10
costs["C"] = 100
costs["D"] = 1000

which_room = {}
which_room["A"] = 0
which_room["B"] = 1
which_room["C"] = 2
which_room["D"] = 3

def non_empty(room):
    b = False
    for i in range(n):
        b = b or room[i] != "."
    return b

def print_config_2(config):
    
    print("#############")
    s = "#"
    for x in config[1]:
        if x == ".":
            s += "."
        else:
            s += x
    print(s)
    s1 = "###"
    s2 = "  #"
    for room in config[0]:
        s1 += room[0]
        s2 += room[1]
        s1 += "#"
        s2 += "#"
    s1 += "##"
    s2 += "  "
    print(s1)
    print(s2)
    print("  #########  ")


def print_config(s):
    c = destringify(s)
    if n == 2:
        print_config_2(c)
    else:
        print_config_4(c)

def print_config_4(config):
    print("#############")
    s = "#"
    for x in config[1]:
        if x == ".":
            s += "."
        else:
            s += x
    print(s)
    s1 = "###"
    s2 = "  #"
    s3 = "  #"
    s4 = "  #"
    for room in config[0]:
        s1 += room[0]
        s2 += room[1]
        s3 += room[2]
        s4 += room[3]
        s1 += "#"
        s2 += "#"
        s3 += "#"
        s4 += "#"
    s1 += "##"
    s2 += "  "
    s3 += "  "
    s4 += "  "
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print("  #########  ")

def move_to_room(config):
    rooms = config[0]
    hallway = config[1]
    # Everybody on the hallway can maybe go to his room
    configs = []
    for i in range(len(hallway)):
        x = hallway[i]
        nrooms = [[z for z in y] for y in rooms]
        nhallway = [y for y in hallway]
        nhallway[i] = "."
        if x != ".":
            # We try to move x to its room
            # Is its room free?
            iroom = which_room[x]
            center = 2 + 2 * iroom
            r = nrooms[iroom]

            # Room should be of shape [".", ".", x, x]
            j = 0
            while j < n and r[j] == ".":
                j += 1
            b = True
            while j < n:
                b = b and r[j] == x
                j += 1
            if b:
                floor = n - 1
                while floor > 0 and r[floor] != ".":
                    floor -= 1
                # After the loop:
                # r[floor] = "."
 
                # Only way that it can go in
                # Moreover, is the path to this room free?
                free = True
                a = min(i, center)
                b = max(i, center)
                for j in range(a, b + 1):
                    free = free and nhallway[j] == "."
                if free:
                    # So this is free
                    cost = (b - a) * costs[x]

                    cost += (floor + 1) * costs[x]
                    nrooms[iroom][floor] = x
                    
                    configs.append((cost, stringify((nrooms, nhallway))))
    return configs

# The top one from the room is not in the right room
# Or it is in the right room, but below it is wrong
def wrong_room(r, x):
    # We know it's non-empty
    j = 0
    while r[j] == ".":
        j += 1
    if r[j] != x:
        return True
    else:
        j += 1
        while j < n:
            if r[j] != x:
                return True
            j += 1
        return False


which_room_rev = ["A", "B", "C", "D"]

# Config = (score, rooms, hallway)
def move_from_room(config):
    rooms = config[0]
    hallway = config[1]
    # Can we move 0?
    # 3, 5, 7, 9
    configs = []
    for i in range(4):
        center = 2 + 2 * i
        # Only if wrong room:
        if non_empty(rooms[i]) and hallway[center] == "." and wrong_room(rooms[i], which_room_rev[i]):

            # 1. Move to center
            cost = 0
            nrooms = [[x for x in y] for y in rooms]

            # How much to climb?

            j = 0
            while nrooms[i][j] == ".":
                j += 1
            x = nrooms[i][j]
            nrooms[i][j] = "."

            cost += costs[x] * (j + 1)

            # Currently at the center



            # Can we move it directly to its room
            # nrooms = [[z for z in y] for y in rooms]
            nhallway = [y for y in hallway]

            # TODO: Redo this
            # nhallway[i] = "."

            done = False

            # We try to move x to its room
            # Is its room free?
            iroom = which_room[x]
            new_center = 2 + 2 * iroom
            r = nrooms[iroom]

            # Room should be of shape [".", ".", x, x]
            j = 0
            while j < n and r[j] == ".":
                j += 1
            b = True
            while j < n:
                b = b and r[j] == x
                j += 1
            if b:
                floor = n - 1
                while floor > 0 and r[floor] != ".":
                    floor -= 1
                # After the loop:
                # r[floor] = "."
 
                # Only way that it can go in
                # Moreover, is the path to this room free?
                free = True
                a = min(new_center, center)
                b = max(new_center, center)
                for j in range(a, b + 1):
                    if j != center:
                        free = free and nhallway[j] == "."
                if free:
                    # So this is free
                    cost += (b - a) * costs[x]

                    cost += (floor + 1) * costs[x]
                    nrooms[iroom][floor] = x

                    done = True
                    configs.append((cost, stringify((nrooms, nhallway))))
            if not done:
                possibilities = []
                # First we go left
                for p in range(center - 1, -1, -1):
                    if hallway[p] != ".":
                        break
                    possibilities.append(p)

                for p in range(center + 1, 11):
                    if hallway[p] != ".":
                        break
                    possibilities.append(p)

                # Forbidden: 2, 4, 6, 8
                possibilities = [p for p in possibilities if p not in [2, 4, 6, 8]]
                

                for p in possibilities:
                    # nrooms = [[p for p in y] for y in nrooms]
                    # Moving from center to p
                    nhallway = [y for y in hallway]
                    nhallway[p] = x
                    configs.append((cost + abs(p - center) * costs[x], stringify((nrooms, nhallway))))

    return configs
    
def is_complete(config):
    rooms = config[1]
    b = True
    for x in ["A", "B", "C", "D"]:
        i = which_room[x]
        for j in range(n):
            b = b and (rooms[i][j] == x)
    return b

def exist_complete(configs):
    for c in configs:
        if is_complete(c[1]):
            return True
    return False

def print_configs(configs, fscore=None):
    for i in range(len(configs)):
        if fscore is None or configs[i][0] == fscore:
            print()
            print(i)
            print_config(configs[i])

# Must be sound
def estimate_manhattan(config):
    cost = 0
    rooms = config[0]
    hallway = config[1]
    to_pay = {}
    to_pay["A"] = 0
    to_pay["B"] = 0
    to_pay["C"] = 0
    to_pay["D"] = 0

    for i in range(len(hallway)):
        x = hallway[i]
        if x != ".":
            iroom = which_room[x]
            center = 2 + 2 * iroom
            cost += costs[x] * (abs(i - center) + 1)

            cost += to_pay[x] * costs[x]
            to_pay[x] += 1

    for i in range(len(rooms)):
        r = rooms[i]
        for j in range(n):
            x = r[j]
            if x != ".":
                incorrect_room = (i != which_room[x])
                # Wrong if something < j is not x
                for k in range(j + 1, n):
                    incorrect_room = incorrect_room or (r[k] != x)

                if incorrect_room:
                    # Not the correct room
                    # Cost of getting out of the room
                    cost += (j + 1) * costs[x]

                    iroom = which_room[x]
                    old_center = 2 + 2 * i
                    new_center = 2 + 2 * iroom
                    cost += costs[x] * (abs(new_center - old_center) + 1)

                    cost += to_pay[x] * costs[x]
                    to_pay[x] += 1

    return cost

def destringify(s):
    hallway = []
    rooms = []
    for i in range(11):
        hallway.append(s[i])
    for i in range(4):
        r = []
        for j in range(n):
            r.append(s[11 + i * n + j])
        rooms.append(r)
    return (rooms, hallway)

def stringify(config):
    rooms = config[0]
    hallway = config[1]
    s = "".join(hallway)
    for r in rooms:
        for x in r:
            s += x
    return s



last = "..........."


for x in ["A", "B", "C", "D"]:
    for _ in range(n):
        last += x

final_scores = {}
final_scores[last] = 0

# Maybe add back the fact that we can move directly to another room

succ = {}
succ[last] = None

# Current_min = we don't care about this one?
def compute_cost(s0, current_min):
    print(len(final_scores))
    if s0 not in final_scores:
        conf = destringify(s0)

        # All possible moves
        mini = 100000000000
        for (added_cost, s) in move_from_room(conf) + move_to_room(conf):
            lower_bound = added_cost + estimate_manhattan(destringify(s))
            if lower_bound < current_min:
                score = added_cost + compute_cost(s, mini)

                # print("Original", s0)
                # print("Destination", s)
                # print("Cost", added_cost)


                assert(score >= lower_bound)
                if score < mini:
                    mini = score
                    succ[s0] = s

            # if s not in estimates:
             #   estimates[s] = estimate_manhattan(destringify(s))
            #if s not in scores or score < scores[s]:
             #   scores[s] = score
             #   to_see.add(s)
             #   assert(scores[c] + estimates[c] <= scores[s] + estimates[s])
        final_scores[s0] = mini

    return final_scores[s0]

print(compute_cost(s0, 100000000000000))

l = []

current = s0
while current != None:
    l.append(current)
    current = succ[current]

for i in range(len(l) - 1):
    print_config(l[i])
    print()
    print("Cost:", final_scores[l[i]] - final_scores[l[i+1]])
    print()

print_config(l[-1])








c0 = destringify(s0)

scores = {}
scores[s0] = 0
parent = {}
parent[s0] = None

estimates = {}
estimates[s0] = estimate_manhattan(c0)

to_see = set([s0])


seen = set()

def iterate():
    pscore = 1000000000
    c = None

    for cand in to_see:
        scand = scores[cand] + estimates[cand]
        if scand < pscore:
            pscore = scand
            c = cand

    seen.add(c)


    to_see.remove(c)
    conf = destringify(c)

    for (added_cost, s) in move_from_room(conf) + move_to_room(conf):
        if s not in seen:
            score = scores[c] + added_cost
            if s not in estimates:
                estimates[s] = estimate_manhattan(destringify(s))
            if s not in scores or score < scores[s]:
                parent[s] = c
                scores[s] = score
                to_see.add(s)
                assert(scores[c] + estimates[c] <= scores[s] + estimates[s])

def first_approach():


    i = 0
    #for _ in range(100000):
    #min_score = scores[s0] + estimates[s0]
    while last not in scores:
        i += 1
        print(i, len(to_see))
        iterate()

    def path_to(s):
        current = s
        path = []
        while current != None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path
            

    print(scores[last])

    print(path_to(last))


#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########


