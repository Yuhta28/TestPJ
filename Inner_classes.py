# Inner class
class Human2:
    def __init__(self):
        self.name = "George"
        self.head = self.Head2()

    class Head2:
        def talk(self):
            return "talking2"
if __name__ == '__main__':
    geroge = Human2()
    print(geroge.name)
    print(geroge.head.talk())

# Multiple inner classes
class Human:
    def __init__(self):
        self.name = "Guido"
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            return "talking..."

    class Brain:
        def think(self):
            return "thinking..."

if __name__ == "__main__":
    guido = Human()
    print(guido.name)
    print(guido.head.talk())
    print(guido.brain.think())