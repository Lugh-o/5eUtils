import random as rand

def roll(sides, number):
    if sides <= 0 or number <= 0:
        return "Invalid input. Please enter valid numbers.\n"
    seq = list(range(1,sides+1))
    result = []
    for _ in range(number):
        result.append(rand.choice(seq))
    return result
