def combsort(given):
    space = len(given) - 1
    while space >= 1:
        for j in range(len(given) - space):
            if given[j] > given[j + space]:
                given[j], given[j + space] = given[j + space], given[j]
        space = int(space // 1.247)
    return given
