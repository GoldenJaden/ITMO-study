import math

example = [24, -79, -85, -99, 79, -24, -22, -100, 24, 74, 75, 41, -12, -9, -55, -90, -1, -17, -16, -1]
need = True
steps = 3
while need:
    need = False
    steps += 3
    for i in range(len(example) - 1):
        steps += 2
        if example[i] > example[i + 1]:
            example[i], example[i + 1] = example[i + 1], example[i]
            need = True
            steps += 4
print(example)
print(steps)
print(len(example) * math.log(len(example)))
#Сложность n^2



