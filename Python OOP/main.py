# OOP
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))

# Everython in Python are Objects, Object Oriented Programming is a paradigm, it says you can write code in a object and classes format,
# Its a way to structure the code, it really helpful in writting big codes

# -------- OOP 2 -----------
# Everything in Python are objects, using classes and objects we are able to create our own types, methods and attributes
# What exactly is OOP?
# Object Oriented Programming is a paradigm or we say its a way to structure our code
# up until now we just do the procedural programming (Do this Do that)[Action oriented]

# Class - class is an blueprint or map of what we are going to create ? What properties or attributes are in there
# so using this bluprints or class we create a structure or format for objects(represent the real world entity)
# For Ex
# Student is a class, its a structure or format for student entity, what things we need for student(roll no, student name, course, DOB etc) this all variables are define in Student class so in future new stuudent are comes in they use same structure
# Class
# So class == Category == Type and class is an description of an object, its an blueprint
# Using classes we instantiate the instances, we create a objects using classes
# Object
# Object is a real world entity and its properties and behaviour are defined in class


class Student:
    pass


s1 = Student()
# print(type(s1))

# -------------Write our first programe----------
# game players


class PlayerCharacter:
    def __init__(self, name):  # constructor
        self.name = name  # its an attribute

    def run(self):  # method
        print('Run!!!')


# lets instanciate
player1 = PlayerCharacter('ashwin')
# player1.name = 'rahul'
# print(player1.name)# Attributes
player1.run()  # method

player2 = PlayerCharacter('pratik')
# Every objects are placed on different location


# self : self is just referencing to the instance(object) of class, so player1 is just reference to the self that way it makes dynamic, so player1.name is nothing but a self.name

# ---------Attributes and methods--------------
# print(help(list))  # it reurn the bluprint of the class

# Attributes are the piece of data that are dynamic to the object, object is unique to the attributes


class PlayerCharacter:
    membership = True  # class object attributes, its a fixed value and not vary

    def __init__(self, name, age):  # constructor
        if PlayerCharacter.membership:
            self.name = name  # its an attribute
            self.age = age

    def run(self):  # method
        print('Run!!!')

    def greet_player(self):
        return f'Welcome {self.name}'


player3 = PlayerCharacter('simin', 25)
player3.membership = False
player3 = PlayerCharacter('simin', 25)
print(player3.greet_player())

# ----------Init----------
# __init__ called when instantiate the object
# player1 = PlayerCharacter()


# --------------classmethod vs staticmethod-------------
# class method


class Student:
    rollNo = 20

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # @classmethod
    # def adding_things(cls, num1, num2):
    #     return num1 + num2

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('rahi', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# ashwin = Student('ashwin', 27)
# we can access class method using class name it dont require to instanciate
student1 = Student.adding_things(20, 23)
print(student1.age)
#  we can create intsance using class method also

# Static method
print(Student.adding_things2(1, 2))
# static method doesn't care it instanciate or not it work on both class as well as instances
print(student1.adding_things2(5, 6))

# Reviewing what we know so far


# ---------------Developer Fundamentals 5----------
# Test your assumptions
# it says whereever you are learning from, whatever you are learning just test it out, just get the understanding what you are learning.


# --------Encapsulation--------
# There is the 4 pillars of OOP
# 1 Encapsulation
# 2 Abstraction
# 3 Inheritence
# 4 Polymorphism

# the idea behind encapsulation is binding all data and methods for manipulating the data
# or package the information into a bundle that is class, we store the data in capsule format.

class Encapsulated:
    def Encapsulation():
        print('this is the example of encapsulation!')

# here we bundle our data and methods in a capsule format, write it once and use it multiple time.

# ------------Abstraction-------------
# Hiding information or abstracting away information, giving access the necessary things.


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def apponted(self):
        print('you are appointed as a teacher')


mathTeacher = Teacher('Diksha', 25)
# but this way anyone can come and edit the information we need something that gave us a protection
mathTeacher.apponted = 'Not appointed'
print(mathTeacher.apponted)


# -----------private Variable and Public Variable--------------

# as above we see that anyone can come and do some changes, so that is the issue and for that there is the idea of Private vs public variable
# In java programming language there is a private keyword but in python they didt have any private thing they have just a naming convention

class Car:
    def __init__(self, color, model):
        self._color = color
        self._model = model

# here single underscore variable is stated that its a private variable in python, but still we can edit because developer set a convention like __init__ double underscore is called a Dunder method that says its a private so dont touch this.

# -------------Inheritence-------------

# inheritence is very useful in oop concept, we can use class feature to another class by inheriting the Name, it just like parent child, theres also called Subclasses and Derived classes.


class User:
    def logged_in(self):
        print('You are logIn Successfully.')


class Wizard(User):  # its inheriting from User subclass
    pass


class Archer(User):
    pass


wizard1 = Wizard()
archer1 = Archer()
wizard1.logged_in()  # here we can access parent class method
archer1.logged_in()

# --------------inheritence 2 ----------------
# isinstance(object, class) # This way we check its a object or not
print(isinstance(wizard1, object))
# so object is python inbuilt class because everything in python are objects, if you see extra dunder methods actually it comes from object class(Base class) so we actualy inherit from object class.

# -------------PolyMorphism-----------

# poly means many and morphism means forms, Many Forms

# Sharing same method name Just like local or global variable, same method name but its dynamic based on there objects attribut. Lets see


class User:
    def logged_in(self):
        print('You are logIn Successfully.')

    def attack(self):
        print('do nothing')


class Wizard(User):  # its inheriting from User subclass
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f'attacking with arrows: left- {self._num_arrows}')


fireWizard = Wizard('fire', 50)
archero = Archer('Archero', 100)

# Same method name but action are different based on objects attribute
fireWizard.attack()
archero.attack()


def player_attack(char):
    char.attack()


player_attack(fireWizard)
player_attack(archero)

for char in [fireWizard, archero]:
    char.attack()


# --------------super()----------------
class Player:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('You are a player12223')


class Wizard(Player):  # its inheriting from Player subclass
    def __init__(self, name, power, email):
        # Player.__init__(self, email)
        # another way
        super().__init__(email)
        self._name = name
        self._power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self._power}')


# here when we inherit class the attributes are not by default we need to call them
wizardo = Wizard('wizardo', 50, 'amail@email.com')
print(wizardo.email)

# ----------object introspection----------
# ability to determine the type of an object at the run time
# using this we inspect the objects, its attributes, methods etc.
# print(dir(wizardo))

# ------------Dunder Method----------
# dunder means double underscore its a special methods that come from python base class OBJECT
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
#  above all are the base class object methods


class Toy(object):
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_list = [1, 2, 3, 4, 5]

    def __str__(self):  # print(str(action_figure))
        return self.color

    def __len__(self):  # print(len(action_figure))
        return 5

    # def __del__(self):  # del action_figure
    #     print('deleted !')

    def __call__(self):  # action_figure()
        return 'yess!'

    def __getitem__(self, i):  # print(action_figure[2])
        return self.my_list[i]

    def __repr__(self):  # print(repr(action_figure))
        return str(self.age)

    def __hash__(self):  # print(hash(action_figure))
        return 10


action_figure = Toy('red', 20)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure[2])
print(repr(action_figure))
print(hash(action_figure))
# del action_figure

# print(dir(action_figure))


# -------------multiple inheritence------------


class GameCharacter:
    def logged_in(self):
        print('You are logIn Successfully.')

    def attack(self):
        print('do nothing')


class Wizard(GameCharacter):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with power of {self._power}')


class Archer(GameCharacter):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self._num_arrows} remaining')

    def run(self):
        print('running !!!')


class HybridBorg(Wizard, Archer):  # multiple inheritence
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


hb1 = HybridBorg('archero', 60, 100)

print(hb1.check_arrows())
print(hb1.attack())
print(hb1.run())

# ----------MRO(method resolution order)-------------
# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.


class A(object):
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(C, B):
    pass


print(D.num)
print(D.mro())


# ##########################OOPs in Python Completed##########################
