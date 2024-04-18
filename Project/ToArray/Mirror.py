transform = {0: 56, 1: 48, 2: 40, 3: 32, 4: 24, 5: 16, 6: 8, 7: 0}

def mirror(posList):
    
    l = 71*[0]

    for i in range(64):
        l[i] = posList[transform[(i // 8)] + (i % 8)]

    for i in range(7):
        l[64 + i] = -1 * posList[64 + i]

    return l
    