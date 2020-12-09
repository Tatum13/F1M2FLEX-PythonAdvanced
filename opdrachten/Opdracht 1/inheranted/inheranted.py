class Character :

    speed = 10
    points = 0
    sprite = None

    def Walk(self) :
        print("Character loopt nu met snelheid", self.speed)


class Mario (Character) :

    lives = 3
    item = None

    def Jump(self) :
        print("Mario springt!")


CharacterA = Character()
marioX = Mario()


CharacterA.Walk()
marioX.Walk()

print(CharacterA.speed)
print(marioX.speed)
print(marioX.lives)