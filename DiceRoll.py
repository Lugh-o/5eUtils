import random as rand

def roll(sides, number):
    seq = list(range(1,sides+1))
    result = []
    for _ in range(number):
        result.append(rand.choice(seq))
    return result
