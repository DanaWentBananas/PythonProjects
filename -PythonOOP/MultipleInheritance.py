# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "im A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "im B"


class C(A, B):
    def __init__(self):
        super().__init__()
        
    def show(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()

#method resolution order
print(C.__mro__)

