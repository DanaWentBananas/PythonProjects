#creating class
class Book:
    
    #shared class properties
    booktypes= ("hardcover","paperback","ebook")
    
    #gets called when instance is created
    def __init__(self,title,author,price,booktype):
        self.title = title
        self.author = author
        self.price = price
        
        self.__secret = "this is a secret"
        
        #accessing shared class attribute
        if(booktype not in Book.booktypes):
            raise ValueError(f'{booktype} not valid')
        else:
            self.booktype = booktype
    
    #shared class method
    @classmethod
    def getBooktype(cls):
        return cls.booktypes
    
    __booklist = None
    
    #method can be accessed everywhere
    @staticmethod
    def getBooklist():
        if Book.__booklist==None:
            Book.__booklist = []
        return Book.__booklist
        
    #instance methods
    def getAuthor(self):
        
        #check if discount exists
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.author
        
    def setTitle(self,newTitle):
        self.title = newTitle
    
    def discount(self,amount):
        #hint that its a class variable
        #that it might not even exist if this method was not called
        self._discount = amount
    
    
        
#creating instance of class
b1 = Book("art of war","poop",20,"hardcover")
b2 = Book("war and peace","ding",33,"ebook")

#print class
print(b1)
print(b1.getAuthor())

#accessing secret class variables
print(b1._Book__secret)

print(b1.getBooktype())


print(Book.getBooklist)