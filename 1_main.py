M = [int(x) for x in open("1_input.txt", "r").readlines()]

c = 0
for i in range(len(M) - 1):
    if M[i+1] > M[i]:
        c = c + 1
print(c)

c = 0
for i in range(len(M) - 3):
    if M[i+3] > M[i]:
        c = c + 1
print(c)
