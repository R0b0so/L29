from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk")
class snake(animal):
    def move(self):
        print("I can slither")
class turtle(animal):
    def move(self):
        print("I can crawl")
class fish(animal):
    def move(self):
        print("I can swim")
h = human()
h.move()
s = snake()
s.move()
t = turtle()
t.move()
f = fish()
f.move()






