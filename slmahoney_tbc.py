#sabrina mahoney
#tbc

def takeDamage(hero, damage):
    hitPoints -= max(maxDamage - armor)
    
def isAlive(hero):
    return hitPoints > 0

def testInt(self, value, min = 0, max = 100, default = 0):

    out = default

    if type(value) == int:
        if value >= min:
            if value <= max:
                out = value 
            else:
                print("Too large")
        else:
            print("Too small")
    else:
        print("Must be an int")

    return out
def hitChance(hero, monster):
    damage  = hitPoints - maxDamage (random.randint (0, 100))
    
def battle (hero, enemy):
    while hero(isAlive) and monster(isAlive)
    hero(takeDamage)
    if monster(isAlive)
    monster(takeDamage)
    
    if player(isAlive):
        print (f"{hero} wins!)
        
    else:
        print (f"{monster} wins!)
        
print:
    "press for another round:"
    "knight hits dragon"
    "knight (hero.hitPoints) HP"
    "dragon hits knight"
    "dragon (monster.hitPoints) HP"