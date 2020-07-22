class C:
    def __init__(self):
        print('class C instance has been created')
        self.name = 'ccc'
        self.age = 0
    def say_hi(self):
        print('hi')
    def add_age(self,n:int):
        self.age +=n
    def __str__(self):
        return "__str__is recalled"
    def __repr__(self):
        return "__repr__is recalled"
    def __abs__(self):
        print("__abs__is recalled")
    def __len__(self):
        print("__len__ is recalled")
    def __add__(self,other):
        return self.age+other.age
