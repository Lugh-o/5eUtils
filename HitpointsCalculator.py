import DiceRoll

def getHitdie(characterClass):
    #hitdie[0] -> die
    #hitdie[1] -> avg
    match characterClass:
        case "Wizard" | "Sorcerer":
            hitDie = [6, 4]
        case "Artificer" | "Bard" | "Cleric" | "Druid" | "Monk" | "Rogue":
            hitDie = [8, 5]
        case "Fighter" | "Paladin" | "Ranger": 
            hitDie = [10, 6]
        case "Barbarian":
            hitDie = [12, 7]
        case _:
            return -1
    return hitDie

def classLevelUp(hitDie, conMod, useAverage, hasTough, isHillDwarf, isFirst):
    #hitdie[0] -> die
    #hitdie[1] -> avg
    if isFirst:
        hpIncrease = hitDie[0] + conMod
    elif useAverage:
        hpIncrease = hitDie[1] + conMod
    else:
        hpIncrease = DiceRoll.roll(hitDie[0], 1) + conMod
    
    if isHillDwarf:
        hpIncrease += 1
        
    if hasTough:
        hpIncrease += 2
    
    if hpIncrease < 0:
        hpIncrease = 1
        
    return hpIncrease
   
def hpCalc(characterClass, conMod, useAverage, hasTough, isHillDwarf, level):
    hitDie = getHitdie(characterClass)
    hpTotal = classLevelUp(hitDie, conMod, useAverage, hasTough, isHillDwarf, True)
    for _ in range(level-1):
        hpTotal += classLevelUp(hitDie, conMod, useAverage, hasTough, isHillDwarf, False)
    return hpTotal