# First iteration
w = 5
# Input

def iter0(w, z):
    if w - 14 != z % 26:
        z *= 26
        z += w + 8
    return z

