class Organism:
    alive = True
class Animals(Organism):

    def eat(self):
        print('This animal is Eating')

class Rabbit(Animals):
    def run(self):
        print('This rabbit is Running')

class Fish(Animals):
    def swim(self):
        print('The fish is Swimming')
class Hawaki(Animals):
    def fly(self):
        print('The hawk is Flying')
rabbit = Rabbit()
fish = Fish()
hawaki = Hawaki()
rabbit.eat()
hawaki.fly()
fish.swim()
# mjj====================================================
class Prey:
    def flee(self):
        print('The prey is Fleeing')
class Predator:
    def hunt(self):
        print('The predator is hunting')
class Rabbiti(Prey):
    pass
class Fishi(Prey,Predator):
    pass
class Hawk(Predator):
    pass
rabbiti = Rabbiti
fishi = Fishi()
hawk  = Hawk
# rabbiti.flee()
fishi.flee()
fishi.hunt()
# ;=========================================
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
class Square(Rectangle):
    def __init__(self, width, length):
       super().__init__(width, length)
    def area(self):
        return self.width * self.length
class Cube(Rectangle):
    def __init__(self, width, length, height):
      super().__init__(width, length)
      self.height = height
    def volume(self):
        return self.width * self.length * self.height
square = Square(5, 5)
cube = Cube(5, 5, 9)
print(square.area())
print(cube.volume())


