from logic import Logic

def NumberOfHeroesInput():
    numHeroes = 0
    while numHeroes > 7 or numHeroes < 1:
        print("\n\n")
        n = input(Logic.NumberOfHeroesText())
        try:
            numHeroes = int(n)
        except ValueError:
            continue
    return numHeroes
def FullProgram():
    heroes = Logic.GetHeroes(NumberOfHeroesInput())
    ship = Logic.GetShip()
    threat = Logic.GetThreat()
    PrintOut(heroes, ship, threat)
def PrintOut(heroes, ship, threat):
    seperator = "---------------"
    print("")
    print("")
    print("Heroes")
    print(seperator)
    print(*heroes, sep="\n")
    print("")
    print("The Raptor")
    print(seperator)
    print(*ship, sep="\n")
    print("")
    print("The Mission")
    print(seperator)
    print(threat)

#MAIN
print(*Logic.OpeningSpiel(), sep="\n")

goAgain = True
while goAgain:
    FullProgram()
    print("")
    goAgain = input("Run again? (y/n)")
    print("")
    print("")
    goAgain = True if goAgain is "y" else False

exit = input("Press any key to quit")
quit()
