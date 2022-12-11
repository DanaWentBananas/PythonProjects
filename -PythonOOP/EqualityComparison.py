# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        
    #EQUALITY MAGIC METHOD
    def __eq__(self,value):
        if not isinstance(value,Book):
            raise ValueError("cant compare")
        
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)
    
    
    #COMPARISON MAGIC METHOD, theres more for others
    def __ge__(self,value):
        if not isinstance(value,Book):
            raise ValueError("cant compare")
        
        return self.price <= value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

#checks location, wont be right 
print(b1==b3)

print(b1<=b2)

#WE CAN SORT USING THESE COMPARISONS
#put them in a list and sort()
