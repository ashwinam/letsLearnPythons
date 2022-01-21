# print('Hello World!')
# -----------------------------------------
# # data types is just a Values in Python or tell the computer how to interpret the values
# # Fundamental Data Types
# int
# float
# str
# bool
# list
# set
# tuple
# dict

# # Custom data types using classes

# # specialized data types (modules)

# None # Nothing, absence of value or 0 in mathematical term

# #using data types we manipulate the values like create, store, update & delete and with we tell computer to perform some actions


# # Numbers (int & float)

# int # integer = whole number 0,1,2,3,4,5
# float # floating point number with a decimal point 0.1,0.2,5.1,3.2

# #------------------- Numbers------------------
# int 
# float
# 2 + 4 # did't recognise what 2+4 is? so, python as a language give us a specification for what you want to do with 2+4 for ex if you want to print then just print(2+4)
# # print(2+4) # it is just an action we tell computer perform this action using python

# # Some common mathematical operation
# print(2 + 4) # Addition
# print(2 - 4) # Subtraction
# print(2 / 4) # Division 
# print(2 * 4) # Multiplication

# # Some extra arithmatic operators
# print(2 ** 4) # Exponent 2 to the power 4(2^4)
# print(2//4) # floor division return in int quotient not an floating point number
# print(2 % 4) # modulo it returns the remainder

# # lets check data types using type()

# print(type(2+4))
# print(type(2-4))
# print(type(2*4))
# print(type(4/4))
# print(type(2//4))

# #  Why we need float in the first place?
# # so every data type take space in memory and float take more memory than integer ,with float computer create two spaces before decimal point and after decimal point(10.56 so 10 create different memory and 56 created difrent memory in binary format)
# print(9.9+1.1, type(9.9+1.1))

# ----------Math Funstions-------------
# function is a action (it means telling the computer what you want me to do for you like a servant[print is an function ,type is an action])

# print(round(2.6))
# print(abs(-20)) # return the positive integer value

# ----------------Developer Fundamental - I-----------
# Be the unique person or programmer that everyone wants

# 1) Don't Read Dictionery 
# it means every beginner try to learn everything but its not the right way
# You need to know where to use which thing and need to learn googling skill
# dont try to learn language like you need to earn 100% in a test don't do that
#  use thereference or google it, what need for the specific task.


# -----------------Operator Precedence 11/01/2022----------

# It is an mathematical operators(+ - * / ), which thing need to be evaluated first

# Precedence
# ()
# **
# * / 
# + -

# print((5 + 4) * 10 / 2) # 45.0

# print(((5 + 4) * 10) / 2) # 45.0

# print((5 + 4) * (10 / 2)) # 45.0

# print(5 + (4 * 10) / 2) # 25.0

# print(5 + 4 * 10 // 2) # 25

# --------------Extra Data types--------------
# complex # use for complex mathematical opeartions


# bin() # convert int value into binary number system
# print(bin(10)) # 0b1010 represents binary 0b shows binary type after that 1010 is binary

# convert binary into integer
# print(int('0b1010',2)) # in 2 is base value of binary
# base 10 is for decimal, 2 for binary, 8 for octal, 16 for hexadecimal


# -------------Variables------------------12/01/2022

# variable is just an a technical term that pretty much all programming languages have, variable is just a way to store information/data through out the program

# Programs are being data that are been store,that are been changed,that been removed

# using variables we use the values that are in variable able to use anywhere in our program
# for ex
# iq = 190
# it is just like we are binding the 190 to the iq name

# print(iq)

# So there have some best practices to write the Variables or we can say the rules behind writing the variale name in python:
# 1) Snake_case : snake_case is just like seperate the name using underscore for ex 
# user_iq = 190
# print(user_iq)
# 2) Variable name start with the lowercase letters or underscores
# 3) variables included numbers,letters,underscores
# starting variable using underscoes it means in private variable in python
# 4) variables are Case sensitive
# 5) *** Don't overwrite the keywords(the reserved names in python)
# for ex
# print = 190
# print(print) # in here we get the error because interpreter get confused with thing is print( and which print has 190)

# Constants
# constants is the value that never been changed
# ex PI = 3.14 (its a universal truth that pi value is 3.14 so it means its constant)
# Best convention for writing a constant in python is write variable name in capital letters
# PI = 3.14 # although you can change it but its the way to write the constants or tell others programmers this are constants

# Let assign multiple values in one line
# a,b,c = 1,2,3
# print(a,b,c)

# Tips
# * Variable name need to be very descriptive
# * Naming a variable is realy important it makes your code redeable

# -------------Expression vs Statements(technical term)----------
# iq = 100
# user_age = iq/5

# iq / 5 is called an expression because it evaluate down to an single value (20) and other hand the whole line [user_age = iq/5] is called an statements because its not evaluating anything it storing the information.


# -----Augmented Assignment Operator -------
# what does that mean? it's a neat way to calculating addition,subtraction & multipliction Let seee
# for ex
# value = 5 
# value = value + 2 # its a common way to add things in variable
# Short hand of writing [value = value + 2] into this [value += 2]
# Augmented Assignment Operator
# but before applying this there something in variable, in our case value = 5.
# value += 2
# print(value)


# ---------String(< class 'str'>)----------------

# # string is a piece of text or a sentence,its a bunch of characters
# 'Hello there!' # its called a string
# print(type('Hello there!')) #'data type is str'
# # writing strings in a varius ways
# 'Hello there' # in single quotes
# "Hello there" # in double quotes
# long_string = ''' 
# WOW
# 0 0
# ---
# '''
# print(long_string) # its also called multi line string

# there a thing called string concatenation
# its a way to join more than one string and make it one
# first_name = 'ashwin'
# last_name = 'mandaokar'
# full_name = first_name +' '+ last_name
# print(full_name)

# -------------Type Conversion------------
# type conversion is a way to change type of the values
# print(type(int(str(100))))
# in simple manner
# a = str(100)
# b = int(a)
# c = type(b)
# print(c)
# str & int's are the functions in python

# -------Escape sequences or characters----------
# weather = 'it's raint here' # this throws error because python thinks string start by first single quote and end quote assume before s and after sentence it not recognized
# for that 
# weather = "it's rainy here"

# but what i want is to do put more things like:
# weather = "it's "kind of "rainy here" # for that problem we use escape sequences
# weather = "it's \"kind of\" rainy here" #python thinks whatever after the '\' it seems it string or considered
# print(weather)

# following are the few of thems
# 1) \t = Tab
# 2) \n = newline

# sample_string = '\t hi arnab \n nice to meet you!'
# print(sample_string)

# ---------Formatted String----------------

# suppose you are the owner of ecommerce site and you send a email to the different different customers, so its very headache that type each and every customers and its a static way
# for making a dynamic we use formatted string in python but first lets check the normal way

# name = 'johny'
# age = 55

# print('Hi ' + name + '. You are '+str(age) + ' years old!') # it seems more headache that's why python 3 introduce formatted string

# print(f'Hi {name}. You are {age} years old!') # it introduced in python 3.5+

# print('hi {}. you are {} years old!'.format(name, age)) # it is coming from python 2 and it still running in python 3

# using indexes in .format
# print('hi {1}. you are {0} years old!'.format(name, age)) # index starting from 0

# print('hi {new_name}. you are {age} years old!'.format(new_name = 'ashwin', age = 27))

# -------------String indexing(15-1-2022)-------
# string indexing is a concept to access the strings character by using numbers and number start from 0

str # str(string) is an data type in python, its an ordered sequence of characters

'me me me'
# so the above string is stored n memory like this
# content=                      'me me me'
# the way to stored in a memory= 01234567 so its an ordered address of the particular characters of an string ,lets access it

# selfish = 'me me me'
# print(selfish[0]) # using square brackets we access the characters
# if you want to access the 2nd m of an string just use the address
# print(selfish[3])
# if we just print variable name so that means we get the characters from 0-7

# string slicing its a term that we use for grap the some piece of characters from string, using [ ] (square brackets)
# [start:stop:stepover] 
# start is an starting position that we told python pick the characters from this point
# stop is the place to stop on that position don't go forward
# stepover is thing we dont need that numbers locations

# e.x.
# numbers = '01234567'
        #  01234567
# [start:stop:stepover] 
# print(numbers[0:3]) # 012 '3' is the position that we tell the python to stop so thats why it excluded
# print(numbers[0:8:1]) # its a defult one
# print(numbers[0:8:2])
# print(numbers[-1]) # 7 '-' negative indexing is use for reverse values
# print(numbers[:-2]) # 012345
# print(numbers[::-1]) # start from 0 and stop to 8 and stepover the -1 (76543210) it reverse the values

# ------------immutable (do not change)-------
# immutability its a term that says the that this data type value is not changeable using indexing you need to reassign the whole value that way you can change
# ex
# numbers[0]=8 # TypeError: 'str' object does not support item assignment

# -------built-in-function or methods----------
# len('ashwin') # its an built-in-function

# Built-in-function is a type of action that already declare in python language, its an independent and other hand, built-in-methods its also like an built-in-function but its dependent or owned by someone
# e.x.
# quote = 'to be or not to be'

# print(quote.upper()) # this is an method
# print(quote) # its print an original one because the idea is string is an immutable(it didn't change)

# -------Booleans-------------

#  in python its bool, boolean is like as binary it has only two values either 'True' or 'False'

# name = 'ashwin'
# is_cool = False
# is_cool = True
# Booleans is help to control the flow of program
# print(bool(''))

# Exercise: Type conversion
# How the facebook work
# in profile
name = 'ashwin mandaokar'
age = 27
relationship_status = 'Single'
relationship_status = 'it\'s complicated.'
# print(relationship_status)


# write a programe to find out the age by giving the year

# born_year = input('what year were you born? ')
# current_year = 2022
# born_year = int(born_year)

# age = int(born_year) - current_year
# age = abs(age)
# print('the age of this person is', age)
# print('the age of this person is '+ str(age) + '.')
# print(f'the age of this person is {age}')
# print('the age of this person is {}'.format(age))

# ------------List(18/01/2022)-------------
# list is an data type in python, its a ordered sequence of object of any type, it means you can store any type of values in list and it store in memories in sequence.
# its a sequence of items, its array for python
# list is an data structure(it's a way to structure information/data in containers,folders etc.) in, we can perform crud operation

# ex
li = [1,2,3,4,5]
li1 = ['a','b','c','d']
li2 = [1,2.5,'a',True] # you can store of any type

# suppose you go to the amazon.com and put things on your cart

amazon_cart = ['notebooks','sunglasses']
# the idea for accessing the items from list is just like string, in string we access characters, in list we access the items by using indexing

# print(amazon_cart[0]) #list-indexing == string-indexes
# print(amazon_cart[1])
# print(amazon_cart[2])# throws error list item limit is reached
# print(len(amazon_cart))

# --------------List-slicing----------------
# as we see in string slicing [start:stop:stepthrough] same idea is apply in list slicing
string = 'hellooooo'
# print(string[0:3]) # string slicing access the characters

amazon_cart = ['notebooks',
'sunglasses',
'toys',
'grapes']
# print(amazon_cart[0:3]) # list slicing access the objects/items

# List are mutable(changeable) and string are immutable(ot changeable) you can reassign it
# string[0]='a' # TypeError: 'str' object does not support item assignment
amazon_cart[0] = 'laptop'
# print(amazon_cart) # we can change the item of list thats why its mutable 

# print(amazon_cart[0:4]) # whenever we do this it means it creates a copy of original and above one is original

# copying vs modifying 
# print(amazon_cart) #original list
# If you want to copy the original list and make a new one but do not want to change the original one perform the following thing
new_cart = amazon_cart[0:3] # we copy the items n new_cart so it not affect the original list

#  but if you want to access the original one location do this
# new_cart = amazon_cart
# print(new_cart)
# new_cart[0] = 'apple_macbook'
# print(new_cart)
# print(amazon_cart) 
# we create a link to the original lists memory thats why it changes when new list change i.e. lists are mutable

# -------Matrix-------
# matrix is a way to describe multidimensional list/array

matrix = [
  [1,5,1],
  [1,0,1],
  [1,0,1]
]
# lets access the matrix using list indexes
# print(matrix[0][1])

# ---------list methods 1---------

# action that we take on list, its dependable on list data type it means it only work on lists

basket =  [1,2,3,4,5] # list(range(1,6))
# print(basket)

# //adding//
# new_list = basket.append(100) # this thing return none thats why it gives us a None(absence of value)

basket.append(100) # changes the list in-place(it modified the original list from memory) it does not produce any value it just changes internally.
# new_list = basket
# print(basket)


basket.insert(0,500) # its in-place, place value anywhere in list using index[index,value]

basket.extend([6,7,8,9]) # its in-place, it extend the list with new one.
# print(basket)

# //removing//
deleted_value = basket.pop() #its not a in-place , it return a value . its pop out end of the list and using list index it pops out that particular location value
# print(deleted_value)
# print(basket)

basket.remove(500) #In-place, it takes the value not a indexes
# print(basket)

basket.clear() # in-place, clear all list
# print(basket)

# --------list method 2--------

# //search the value in list //

basket = ['a','b','c','d','e','d']
# print(basket.index('a')) # it return the index number of the value
# print(basket.index('d',0,4)) # extra parameters it takes start & stop , it means set a particular range and search for it.
# python keyword is perform some actions
# print('a' in basket)
# print('i' in 'hi') # this peform on string also

# print(basket.count('d')) # count the values occurs in list

# -------list method 3--------
# basket.sort() # In-place, it sort the list in alphabetical order
# print(basket)

# print(sorted(basket)) # its a function, it create the copy of original and sort it. new_list = basket[:] just like this.

basket.copy() # it copies the list(create shallow copy)

basket.reverse() #In-place, it reverse the list

# -----------Common list patterns--------

# print(basket[::-1]) # create a reverse list copy

# using range function create quick range of functions in list
# print(list(range(1,6)))

# .join() its a string method that help to combine list into string.

new_sentence = ' '.join(['hi','my','name','is','ashwin'])
# print(new_sentence)

# --------list unpacking---------
a,b,c = [1,2,3] #it perform a,b,c = 1,2,3
# print(a,b,c)

# but we want to wrap few things and rest in a list for that

a,b,c,*d,e = list(range(1,10))
# print(a,b,c,d,e)

# ----------------None------------
# none is an data type that represent the absence of value

weapon = None
# print(weapon)

# --------Dictionery(20/1/22)----------
# other programming language has hashtable,map,object
# dictionery is an unordered, key value pair
# dictionery is an data structure(way to oraganize data on container[dict])

dictionery = {
  'a':1,
  'b':2,
}
# print(dictionery)
# print(dictionery['c']) # throws error because key is not existed, for avoiding KeyError user .get()method
dictionery = {
  'a':[1,2,3], # list can be writable in inside dictionery
  'b':'hello',
  'x': True
}

print(dictionery['a'][1]) 


my_list = [
  {
  'a':[4,5,6], 
  'b':'hello',
  'x': True
  },
  {
  'a':[1,2,3], 
  'b':'hello',
  'x': True
  }
]

print(my_list[0]['a'][2])
# Q. why dont one data structure thing does everything?
# ----------Developer fundamental III----------

# Understanding the data structure

# 1. really good programers is able to decide what data structure use when.
# 2. When should you use dictionery & list?
#   i. dictionery hold lot more information because of his architecture (key,value pair) 
#   ii. List is ordered & access by index (li[0])
#   iii. if you want to store data that are in-line(ordered sequence) that time use list
#   iv. if you want to store lot more information tht time use dictionery

# ------------Dictionery key----------

my_list = [
  {
  'a':[4,5,6], 
  'b':'hello',
  'x': True,
  'age': 20,
  #'age':55
  # [123]:123
  },
]

# colons left side thing is key and colon right side is values

# - dictionery value hold any sort of data type
# - dictionery key also use int,string, booleans
# - dictionery key is need to be immutable type(not changeable), and need to be unique, that's why list is not workeable 
# - if dictionery key repeated then value would be overwritten.
# print(my_list[0][123]) # TypeError: unhashable type: 'list'
print(my_list[0]['age'])

# --------dictionery methods--------

# print(my_list[0]['var']) # error break the execution for avoid this things use .get method

print(my_list[0].get('var', 404)) # it return the None, but using second parameter we able to give custom message.

# another way to create dictionery
user = dict(name='ashwin')
print(user)

# ---------Dictionery method 2---------------
# print('name' in user)
# print('hello' in my_list[0].values())
# print(user.items())

# user.clear() # In-place, clear the dictionery

user2 = user.copy() # it create the copy of original dictionery
user.clear()
print(user, user2) # user shows blank dictionery

# print(user2.pop('name')) # it takes key as parameter, return the value

# print(user2.popitem()) # it takes last item from dictionery and return the tuple(key, value), usefu to destructively iterate over a dictionery

user2.update({'age':20}) # In-place, update the existing key , if key not available then inserted

# ---------Tuples -----------

# tuple is a list with immutable type(oce it created it's not changeable)
my_tuple = (1,2,3,4,5) 
# print(type(my_tuple))
print(my_tuple)
print(5 in my_tuple)
# tuples
# 1.it makes code safer,faster than list  but it less flexible thats why it doesn't perform sort or reverse action
# 2. tuple is valid key in dictionery{(1,2):[1,2,3]}

# -------tuple 2--------
print(my_tuple[1:2])
x,y,z,*other = (1,2,3,4,5)
print(x,y,z,other)
my_tuple.count(5)# count the item in tuple
my_tuple.index(5) # ite on which indexes

# ----------sets---------

# set is an unordered collection of unique object

mySet = {1,2,3,4,5,5} # theres no duplicasy

mySet.add(100)
mySet.add(2) # it removes the duplicate

# print(mySet[1]) # it not support indexing
mySet2 = mySet.copy()# copy the set
mySet.clear() # in-place, clear the original
print(mySet,mySet2)

# ---------Set2----------
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

# ----------methods---------

# print(my_set.difference(your_set)) # it told you the difference from the my_set perspective
# my_set.discard(5) # it removes the item from set,in-place
# my_set.difference_update(your_set) # in-place, it changes internally the my_set and remo0ves the common one
# print(my_set.intersection(your_set)) # shows common things
# print(my_set.isdisjoint(your_set)) # it checks two sets are unique are not
# print(my_set.union(your_set)) # it uited two sets and remove duplicates
# print(my_set | your_set) # short hand for union
# print(my_set & your_set) # short hand for intersection
print(my_set.issubset(your_set)) # it checks my_set all values are included in your_set
print(your_set.issuperset(my_set)) # checks the your set is the parend of my_set
# remove duplicasy
my_list = [1,2,3,4,5,5]

# print(list(set(my_list)))

# //////////////PYTHON BASICS s 1 completed/////////////////