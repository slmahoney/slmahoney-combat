import tbc

def main():
    hero = tbc.Character()
    hero.name = "Knight"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character("Dragon", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
    
    