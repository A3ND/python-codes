# POLYMORPHISM USING METHODS

class Rectangle:
    #initializer
    def __init__(self, width=0, height=0,):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate area
    def getArea(self):
        return (self.width * self.height)

class Circle():
    #initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate area
    def getArea(self):
        return (self.radius*self.radius*3.142)

shapes = [Rectangle(6,10), Circle(7)]
print("sides of a rectange are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("sides of a circle are", str(shapes[1].sides))
print("Area of a circle is:", str(shapes[1].getArea()))


# POLYMORPHISM USING INHERITANCE
'we can add new data and methods to a class through inheritance. for the situation when we want our derived class to inherit a method from the base class and have different implementation for it.'
class shape:
    def __init__(self): # initializing sides of all shape to 0
        self.sides = 0
    
    def getArea(self):
        pass

class rectangle(shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width*self.height)

class circle(shape):
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return (self.radius*self.radius*3.142)

shapes = [rectangle(6,10), circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of a circle is :", str(shapes[1].getArea()))