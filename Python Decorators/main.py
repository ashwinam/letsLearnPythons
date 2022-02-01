# Decorators
# Functions in python are Called First Class Citizen(you can pass functions around just like other objects, means anything)
# we can use functions as a variable in python

from time import time


def hello():
    print('hello')


# Below, i am passing here a location of function, so it looks like ill giving two name of my hello function if i delete one of them it still workable.
greet = hello

del hello
# hello() # deleted
# Functions are act like a Variables
# greet()

# @decorator So, decorator is like a supercharge for functions, it means it modify,enhance or something do with the functions

# --------------Higher Order Function(HCO)---------------

# HCO means functions who are take functions as a parameter and return the functions.


def my_func(func):
    func()


# ----------------Decorators 2-----------------

# a function that wrap another function and enhance it,modify it or decorate it

# def my_decorator(func):
#     def wrap_up():
#         func()
#     return wrap_up

# @<decorator_name> it a syntax for decorator


# @my_decorator
# def hello():
#     print('Hello')


# hello() #here nothing fancy happen

# so lets make it Fancy
def my_decorator(func):
    def wrap_up():
        print('*************')
        func()
        print('*************')
    return wrap_up


# @my_decorator
def hello():
    print('hello')


# @my_decorator
def bye():
    print('See Ya Later!')


# hello()  # here i am just decorate hello function without rewriting the stuff
# bye()

# lets Demystify @Decorator
# this is the decorator, it looks confusing thats why python says use @ as a decorator
a = my_decorator(hello)
a()


# ----------Decorators 3---------------

# passing multiple parameters

def decorator(fn):
    def wrapper(*args, **kwargs):
        # Do something here
        fn(*args, **kwargs)  # its a normal function that we create
    return wrapper


@decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hellooooo')

# -----------Why do we need Decorators?-------------
#  lets make something useful


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'time take for this operation {t2 - t1} S')
        return result
    return wrapper


@performance
def operation():
    for i in range(1000000000):
        i * 5


operation()

# ////////////////////Decorators Done////////////////////
