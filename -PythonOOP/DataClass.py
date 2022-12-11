# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass, field
import random

def priceFunc():
    return float(random.randrange(20,40))

@dataclass
class Book:
    #non default always before default
    title: str
    author: str
    
    #default values
    pages: int = 0
    #provides flexibility 
    price: float = field(default=0.0)
    #default factory
    rand: float = field(default_factory=priceFunc)
    
    
    
    #POST INIT, for extra attributes
    def __post__init__(self):
        self.description = f"{self.title} by {self.author}"
        
    
    #YOU CAN ADD FUNCTIONS TOO
    def bookinfo(self):
        return "hello"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

#data class has __repr__
print(b1)

#data class has __eq__
print(b1==b2)


#IMMUTABLE CLASS

@dataclass(frozen = True)
class immutable:
    num1: int = 4
    num2: int = 3
    
    def sth(self,new):
        self.num1 = new
    
obj = immutable()

print(obj)



