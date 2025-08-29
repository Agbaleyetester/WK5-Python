
#Question1
class Book:
     """A simple attempt to model a Book."""  
     def __init__(self, name, publish):
        """Initialize name and age attributes."""
        self.name = name
        self.publish = publish
    # Creating an Object with attribute#
Book1 = Book('Organic Chemistry', '2005')
Book2 = Book('Physical Chemistry', '2001')

print(Book1.name)
print(Book2.publish)

#Question2
class Car:
    def move(self):
        return 'driving'
class plane:
    def move(self):
        return 'flying'
#Polymorphism in action
for motion in [Car(), plane()]:
    print(motion.move())