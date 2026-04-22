# class vehicle:
#     def vehicle_type(self):
#         print("Inside vehicle class")

# #child class
# class Car(vehicle):
#     def car_type(self):
#         print("Inside car class")
# #creating object of child class(car)
# my_car = Car()
# my_car.vehicle_type()  # Inherited method
# my_car.car_type()      # Method of child class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

#     def person_info(self):
#         return f"hi,I'm{self.name} and I'm {self.age} years old"
#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age!r})"
# person1 = Person("Alice", 30)
# person2= Person("Bob", 25)
# print(person1)
# print(person1.greet())
# print(person2.name, person2.age)

# from abc import ABC, abstractmethod

# # The Blueprint (Abstract Base Class)
# class Vehicle(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass

# # Subclasses must implement the mileage method
# class Defender(Vehicle):
#     def mileage(self):
#         return "The mileage of Defender is 7 km/l"

# class Fortuner(Vehicle):
#     def mileage(self):
#         return "The mileage of Fortuner is 10 km/l"

# class Innova(Vehicle):
#     def mileage(self):
#         return "The mileage of Innova is 12 km/l"

# # Creating objects and printing output
# d = Defender()
# print(d.mileage())

# f = Fortuner()
# print(f.mileage())

# i = Innova()
# print(i.mileage())


#POLYMORPHISM
# x="Hello, World!"
# y=['25','Harikirishnan',-10.5,10.9999]
# z=('99.99','meow')
# print(len(x))
# print(len(y))
# print(len(z))
# G={'yak':3,'sparrow':5}
# print(len(G))

#ENCAPSULATION
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private attribute/property
p1 = Person("Alice", 30)
print(p1.name)  # Accessible
# print(p1.__age)  # This would raise an AttributeError
print(p1._Person__age)  # Accessing private attribute (not recommended)