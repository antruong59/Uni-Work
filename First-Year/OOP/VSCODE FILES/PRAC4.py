# task1
class Ant:
    count = 0
    def __init__(self):
        Ant.count += 1
        self.name = f'Ant #{Ant.count}'
        
for i in range(5):
    a = Ant()
    print(a.name)
print(f'There are {Ant.count} ants.')

print('\n')

# task2
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.__width = w
        self.__height = h

    def get_area(self):
        return self.__height * self.__width

    def draw(self):
        for x in range(self.__height):
            print(self.__width * '#')

class HalfSquareTriangle(Shape):
    def __init__(self, b):
        self.__base = b

    def get_area(self):
        return 0.5 * (self.__base ** 2)

    def draw(self):
        for x in range(self.__base):
            print((x + 1) * '*')
            

shapes = [Rectangle(5,3), HalfSquareTriangle(4)]
for x in shapes:
    print(f'A {type(x).__name__} with an area of {x.get_area()}')
    x.draw()
    print()
s = Shape()