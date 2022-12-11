# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    #huh?
    def __getattribute__(self,name):
        if name=="price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            
            return p-(p*d)
        return super().__getattribute__(name)
    
    def __setattr__(self,name,value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError("the price must be float")
            
        return super().__setattr__(name,value)

    #happens when getattribute fails
    def __getattr__(self,name):
        return name + " is not here!"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
