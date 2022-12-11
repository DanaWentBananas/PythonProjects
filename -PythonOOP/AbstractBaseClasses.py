from abc import ABC, abstractmethod

#abstract class
#its like a temmplate for other classes
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
      
    #forces classes that inherit this class to define this method
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
        
    def calcArea(self):
        return 2*self.radius*3.14


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
        
    def calcArea(self):
        return self.side*2

#cant have instance of abstract classes
#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())

