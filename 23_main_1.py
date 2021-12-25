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

def valid_config(config):
    numbers = {}
    numbers["."] = 0
    numbers["A"] = 0
    numbers["B"] = 0
    numbers["C"] = 0
    numbers["D"] = 0
    for x in config[1]:
        numbers[x] += 1
    for r in config[0]:
        for x in r:
            numbers[x] += 1
    b = numbers["."] == 11
    b = b and numbers["A"] == 2
    b = b and numbers["B"] == 2
    b = b and numbers["C"] == 2
    b = b and numbers["D"] == 2
    return b



def non_empty(room):
    return room[0] != "." or room[1] != "."

def print_config(config):
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
        if room[0] == ".":
            s1 += "."
        else:
            s1 += room[0]
        if room[1] == ".":
            s2 += "."
        else:
            s2 += room[1]
        s1 += "#"
        s2 += "#"
    s1 += "##"
    s2 += "  "
    print(s1)
    print(s2)
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
            if r[0] == "." and (r[1] == "." or r[1] == x):
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
                    
                    if nrooms[iroom][1] == ".":
                        cost += 2 * costs[x]
                        nrooms[iroom][1] = x
                    else:
                        cost += costs[x]
                        nrooms[iroom][0] = x
                    assert(valid_config((nrooms, nhallway)))
                    configs.append((cost, (nrooms, nhallway)))
    return configs

def wrong_room(r, x):
    if r[0] != ".":
        return r[0] != x or r[1] != x
    else:
        return r[1] != "." and r[1] != x


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
            if nrooms[i][0] == ".":
                nrooms[i][0] = nrooms[i][1]
                nrooms[i][1] = "."
                cost += costs[nrooms[i][0]]
     
            # 0 is the closest to the surface
            # Thus if we go to a room, we try to go to 1
            x = nrooms[i][0]
            cost += costs[x]
            # nhallway[center] = x
            nrooms[i][0] = "."

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

            for p in possibilities:
                # nrooms = [[p for p in y] for y in nrooms]
                # Moving from center to p
                nhallway = [y for y in hallway]
                nhallway[p] = x
                assert(valid_config((nrooms, nhallway)))
                configs.append((cost + abs(p - center) * costs[x], (nrooms, nhallway)))

    return configs
    
def is_complete(config):
    rooms = config[1]
    b = True
    for x in ["A", "B", "C", "D"]:
        i = which_room[x]
        b = b and (rooms[i][0] == x)
        b = b and (rooms[i][1] == x)
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
    already_paid = set()
    for i in range(len(hallway)):
        x = hallway[i]
        if x != ".":
            iroom = which_room[x]
            center = 2 + 2 * iroom
            cost += costs[x] * (abs(i - center) + 1)

            if x not in already_paid:
                already_paid.add(x)
            else:
                cost += costs[x]

    for i in range(len(rooms)):
        r = rooms[i]
        for j in range(2):
            x = r[j]
            if x != ".":
                incorrect_room = (i != which_room[x])
                incorrect_room = incorrect_room or (j == 0 and r[1] != "." and r[1] != x)

                if incorrect_room:
                    # Not the correct room
                    # Cost of getting out of the room
                    cost += costs[x]
                    if j == 1:
                        cost += costs[x]
                    iroom = which_room[x]
                    old_center = 2 + 2 * i
                    new_center = 2 + 2 * iroom
                    cost += costs[x] * (abs(new_center - old_center) + 1)

                    if x not in already_paid:
                        already_paid.add(x)
                    else:
                        cost += costs[x]

    return cost

def destringify(s):
    hallway = []
    rooms = []
    for i in range(11):
        hallway.append(s[i])
    for i in range(4):
        r = []
        for j in range(2):
            r.append(s[11 + i * 2 + j])
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


# Correct 12111
s0 = "...B......."
s0 += "BACD.CDA"


s0 = "...........BACDBCDA"

s0 = "...........DBDCBAAC"



c0 = destringify(s0)

scores = {}
scores[s0] = 0

estimates = {}
estimates[s0] = estimate_manhattan(c0)

to_see = set([s0])

def iterate():

    pscore = 1000000000
    c = None
    for cand in to_see:
        scand = scores[cand] + estimates[cand]
        if scand < pscore:
            pscore = scand
            c = cand


    to_see.remove(c)
    conf = destringify(c)

    for (added_cost, cc) in move_from_room(conf) + move_to_room(conf):
        s = stringify(cc)
        score = scores[c] + added_cost
        if s not in estimates:
            estimates[s] = estimate_manhattan(cc)
        if s not in scores or score < scores[s]:
            scores[s] = score
            to_see.add(s)
            assert(scores[c] + estimates[c] <= scores[s] + estimates[s])


last = "...........AABBCCDD"

i = 0
#for _ in range(100000):
#min_score = scores[s0] + estimates[s0]
while last not in scores:
    i += 1
    print(i)
    iterate()

print(scores[last])


#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
