f = [line.rstrip() for line in open("20_input.txt").readlines()]
algo = f[0]
image = f[2:]

n = len(image)
m = len(image[0])

def new_pixel(l):
    s = ""
    for x in l:
        if x == "#":
            s += "1"
        else:
            s += "0"
    return algo[int(s, 2)]

def default_pixel(image, i, j, outside):
    if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
        return outside
    else:
        return image[i][j]

def generate_new_image(image, outside="."):
    nimage = []
    for i in range(len(image) + 6):
        nimage.append([])
        for j in range(len(image[0]) + 6):
            l = []
            # Considering i-3 as center
            # (i - 4, i - 1, i)
            # (j - 4, j - 1, j)
            for ii in range(i-4, i-1):
                for jj in range(j-4, j-1):
                    l.append(default_pixel(image, ii, jj, outside))
            nimage[-1].append(new_pixel(l))
    l = [outside for _ in range(9)]
    return (nimage, new_pixel(l))

def print_image(image):
    s = ""
    for line in image:
        s += "".join(line)
        s += "\n"
    print(s)

img = image
o = "."
for i in range(50):
    print(i)
    (img, o) = generate_new_image(img, o)

c = 0
for line in img:
    for x in line:
        if x == "#":
            c += 1
print(c)

