#players = [4, 8]
players = [3, 7]
scores = [0, 0]
turn = 0

# config[p1][p2][s1][s2]

# Instead, count number of times player 1 is at place...
config = [[[[0 for _ in range(21)] for _ in range(21)] for _ in range(10)] for _ in range(10)]
config[players[0] - 1][players[1] - 1][0][0] = 1

def throw_dice():
    results = [0 for _ in range(10)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                results[a + b + c + 3] += 1
    return results

n_wins = [0, 0]

def contains_non_zero(config):
    for a in range(10):
        for b in range(10):
            for c in range(21):
                for d in range(21):
                    if config[a][b][c][d] > 0:
                        return True
    return False

while contains_non_zero(config):
    new_config = [[[[0 for _ in range(21)] for _ in range(21)] for _ in range(10)] for _ in range(10)]
    # Player turn plays
    dices = throw_dice()
    for i in range(10):
        n_dice = dices[i] 
        # Player (turn) rolled an i
        for p1 in range(10):
            for p2 in range(10):
                for s1 in range(21):
                    for s2 in range(21):
                        n = config[p1][p2][s1][s2] * n_dice


                        # New pos
                        if turn == 0:
                            new_pos = p1 + i
                        else:
                            new_pos = p2 + i
                        if new_pos >= 10:
                            new_pos -= 10

                        # Is it a win?
                        if turn == 0 and s1 + new_pos + 1 >= 21:
                            n_wins[turn] += n
                        elif turn == 1 and s2 + new_pos + 1 >= 21:
                            n_wins[turn] += n
                        else:
                            if turn == 0:
                                new_score = s1 + new_pos + 1
                                new_config[new_pos][p2][new_score][s2] += n
                            else:
                                new_score = s2 + new_pos + 1
                                new_config[p1][new_pos][s1][new_score] += n
    config = new_config
    turn = 1 - turn
