from abc import ABC, abstractmethod

#using multiple abstract base classes

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class shape(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def area(self):
        pass
    

class circle(shape, JSONify):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14*2*self.radius
    
    def toJSON(self):
        return f"{{\" circle \" {str(self.area())} }}"
    
c = circle(10)

print(c.toJSON())
