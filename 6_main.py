l = [int(x) for x in open("6_input.txt").readlines()[0].split(",")]

timers = [0 for _ in range(9)]
for x in l:
    timers[x] += 1

for d in range(256):
    new_timers = [0 for _ in range(9)]
    new_timers[8] += timers[0]
    new_timers[6] += timers[0]
    for i in range(8):
        new_timers[i] += timers[i + 1]
    timers = new_timers
print(sum(timers))
