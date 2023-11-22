import DiceRoll

def calcHP(startingDie, conMod, lvlAfterFirst, hasTough, isHillDwarf, useAverage):
    #First level
    hp = startingDie + conMod + hasTough*2 + isHillDwarf
    
    for index, level in enumerate(lvlAfterFirst):
        # lvlAfterFirst= 
        # [Wizard, Sorcerer, Artificer, Bard, Cleric, Druid, Monk, Rogue, Fighter, Paladin, Ranger, Barbarian]
            #hitdie[0] -> die
            #hitdie[1] -> avg
        match index:
            case 0|1:
                hitDie = [6, 4]
            case 2|3|4|5|6|7:
                hitDie = [8, 5]
            case 8|9|10:
                hitDie = [10, 6]
            case 11:
                hitDie = [12,7]
            case _:
                return -1      
            
        if useAverage:
            hpIncrease = hitDie[1] + conMod + hasTough*2 + isHillDwarf
        else:
            diceResult = DiceRoll.roll(hitDie[0], 1)
            if diceResult is str:
                return -1        
            hpIncrease = diceResult[0] + conMod + hasTough*2 + isHillDwarf
   
        if hpIncrease < 0:
            hpIncrease = 1
        
        hpIncrease *= level
        hp += hpIncrease
    return hp
   