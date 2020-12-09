class A:

    speed = 20
    points = 0
    lives = 5
    item = None

    def __init__(self):
        print("punten:", self.points)

    def walk(self):
        print("snelheid:", self.speed)
#-------------------------------------------------------------
class B(A):

    strength = 50
    stamina = 50
    
   def __init__(self):
       print("werkt dit?")

       super().__init__()

   self.speed = 50

   def walk(self):
       print("De snelheid is nu aangepast en is nu geen 20 maar:", self.speed)


class1 = A()
class2 = A()

class1.walk()
class2.lives()
#ik weet niet wat ik  hier fout doe?
   









