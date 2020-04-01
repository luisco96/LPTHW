## Animal is-a object (yes, sort of confusing) look at the e
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def get_name(self):
        print(self.name)

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def get_name(self):
        print(self.name)
    
    def set_height(self, height):
        self.height = height

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary, height):
        ## Init Employee with init method from parent class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        super().set_height(height)

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000, "200 cm")

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover.get_name()

frank.get_name()

mary.set_height("180 cm")

print(mary.height)

print(frank.height)