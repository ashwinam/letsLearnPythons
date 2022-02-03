# -----------Modules In Python-----------
# the idea is that how to organize code
# 1. Python file (.py)
# 2. functions using naming appropriate functions
# 3. classes, The blueprint that we use to create an object

# that way we keep our code Clean, make our code maintainable
# But what if we have seperate files and in that file we have useful functions so how do we use those functions in other files using DRY(Don't repeat Yourself) principle., So idea is called Modules

# Modules in python is nothing but a Python file
# E.x.
'''
1. create a utility.py file
2. write down 2 functions on utility file
(Now I want to use This function in here in Main.py)
For connecting other files in python there is keyword in python(import)
lets import it utility 
'''
# import random
# import random as olala # it works as a alias(used to indicate that a named person is also known or more familiar under another specified name.)
from collections import Counter, namedtuple, defaultdict, deque
import sys
from random import shuffle  # its a good pratice on explicit
import shopping.shopping_cart
import utility

# print(utility)  # it shows the module type and the file location.

# It creates a Pycache folder with .pyc file, so actually it is automatically created by interprter(Cpython) its a compiled file for faster work, when we import the files that time it created. the idea behind is caching(Caching means storing the copies of frequently used data in cache memory so that we can access it faster)
# print(utility.multiply(20, 30))

# -------------packages in Python-------------

# package is just a folder that contains modules(python files), its a way to organize code or big projects

# its comming from the folder so need to connect first folder
# print(shopping.shopping_cart.buy('apples'))

# __init__.py this files python interpreter assumes that it is a package folder.


# # ---------Different Ways to import------------

# from shopping.shopping_cart import buy # here we say <package.module> import <function>
# from shopping import shopping_cart # here <package> import <module>

# from utility import multiply, divide # <module> import <various functions of need>

# from utility import * # its not a good use of *, need to be explicit as above

# #  just make sure that your name is does not collide with inbuilt names


# ---------------__name__----------------
print(__name__)  # it print the file name, if the file is current then it shows __main__, that way we can understand the where the files comes from

# this line says if the file is main then run the programe another way dont run, its helpful in importing.
# if __name__ == '__main__':
#     print('run the programe')


# ---------Python Built in modules-----------

# so its a python files that come with python, thats the main power of python, python is small


# print(random.random()) # generate floating point numbers
# print(random.randint(1, 50)) # generate random integer number it takes start and stop as a argument
# print(random.choice(['apple', 'bananna', 'kiwi', 'watermelon', 'mango'])) # it gives us the choice

my_list = ['apple', 'bananna', 'kiwi', 'watermelon', 'mango']

# In-Place its change original, it shuffles all the items inside the list
shuffle(my_list)
print(my_list)


# -----------python built-in modules 2-----------

# url for all built-in modules (https://docs.python.org/3/py-modindex.html)

# print(sys.argv)
# it takes argument from terminal and return the list with all arguments
first = sys.argv[1:]
print(first)

# -----------Python Package Index(Pypi.org)-----------

# Pypi.org # is a place where third party modules available, we can add our own made Library to this Website
# Standard Library Means Built In Modules

# ----------Pip Install----------
# pip is command that helps to install third party modules from pypi
# python3.9 -m pip --version # for using pip for python 3.9
#

# -----------------Virtual Environment------------------------
# Verisioning dimystify

# 1.1.0 # 0 is a bug fix pdate, # middle 1 is a new release or Added Features # first 1 is breaking Changes and Major changes

# pip3 install pyjokes==0.4.0

# Virtual Environment its like a virtual universe(seperate space/room) where we do anything without interfering outside world
# ----------------Useful modules--------------

# Specialised Data Types
# collections Module: Counter, namedtuple, defaultdict, deque

# 1. Counter : it return the occurences in iterables i dictionery format

occurences = Counter('aaaabbbbbbbvvvvvvvcccccc')
print(occurences)
print(list(occurences.most_common(1)))
print(list(occurences.elements()))


# 2. namedtuple : it's an lightweight object like struct

Point = namedtuple('One', 'x,y')
items = Point(2, 3)
print(items.x, items.y)

# 3. defaultdict : it return the default value if there is no key available

d = defaultdict(lambda: 'does not exist')
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque : double ended Queue (both side operations)

q = deque()
q.append(0)
q.appendleft(2)
q.appendleft(1)
q.pop()
q.popleft()
q.clear()
q.extend([1, 2, 3, 4])
q.extendleft([5, 6, 7, 8])
q.rotate(1)
print(q)
q.rotate(-1)
print(q)


# ---------useful modules2------------
# 1. Datetime 2.time 3.array

# ----------------Developers Fundamentals VI-------------------
# pros & cons of libraries
# importing libraries means more code and file size is more bytes, before do anything ask yourself could i this write be myself?

# /////////////////////Python Modules//////////////////////
