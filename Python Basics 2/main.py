# ////////Python Basics II////////

# Breaking the flow------------
# until now we see the line by line execution
# do something
# do something
# do something

# we don't see the true power of programming or power of machine
# the CONDITIONAL, & CONDITIONAL LOGIC, LOOPS

# machine really do the certain task lot faster than humans.

# ------conditional LOGIC---------(important topic all over programming)

# If & Else

is_old = False
is_licensed = True
# if conditions:
  # statement
# else:
  # statement

# using if statement we able to contrl the flow of the programe

# if is_old:
#   print('You are old enough to drive!')
# else:
#   print('no no no!')

# print('done!')

# if statement executed when the expression is True
# if it false then else part executed or jump out of the if statement

# elif use when you have more than one conditions
# if is_old:
#   print('You are old enough to drive!')
# elif is_licensed:
#   print(' you are not able to drive!')
# else:
#   print('no no no!')

# if is_old and is_licensed:
#   print('You are old enough to drive!')
# else:
#   print('not a chance!')

# ---------Ternary operator(23-01-22)-------
# one line if else condition(short hand for writing if else condition)
# condition _if_True if condition else condition_if_false
# Ex
# is_friend = True
# message = 'message Allowed' if is_friend else "not Allowed"
# print(message)

# ------short circuiting---------
# and # = need both condition True
# or # = need either one condition True

# we mean the stoppage of execution of boolean operation if the truth value of expression has been determined already. The evaluation of expression takes place from left to right. In python, short-circuiting is supported by various boolean operators and functions. 
# ('and' check only False and 'or checks only one 'True' if they get then they return their objects)
# if True or False:
#   print('when "or" get first True it return the object')

# if False and True:
#   print('"and" check the first False then it reutrn the object or exit the if statement ')


# --------Logical operators----------
# and # check the both condition True
# or # check the either condition need to be True
# not # it do the opposite thing not True = False
# > # greater than
# < # less than
# == # equal to
# >= # greater than equal to
# <= # less than equal to
# != # not equal to

# execise
# print (True and True)
# print(True or False)
# print(2 > 5)
# print(1<0)
# print('a' == 'a')
# print(1>=2)
# print(5<=4)
# print( not True)
# print(True != False)

# -----------is vs ==-----------
# == it checks the equality of values
# is = it checks the memory location of values if both same it return True

# print(True == 1) # it try to type conversion bool(1)
# print('' == 1) # here also ssame
# print([] == 1) 
# print(10 == 10.0)
# print([] == [])
a = [1,2,3]
b = [1,2,3]
c = a
# print(a is c)


# --------------Loops[For Loops] (24/01/2022)----------

# loops is programming term that help us to run lines of code over and over again, it is one of the powerful feature of programming language.
# using conditional we skip the lines of code and using loop able to run the code over and over again
# /For loop/
# for item in 'Zero to Mastery': # in here its almost like an if statement but the difference is we use for keyword and 'item' is an a variable and 'Zero to Mastery is an iterable'
#   print(item)

# \lets do nestede loop\

# for item in (1,2,3,4,5):
#   for each_item in ['a', 'b', 'c']: # when this loop execute all, i mean when he done print a b c then it goes to parent loop and took one item and come back here and again do the same process over and over again
#     print(item,each_item)

  # ----------iterables----------
  # iterable = its object or collection that can be iterate over like as (list, tuple, set, string, dictionery)
  # iterated = one by one check each item in the collection.(do repeatedly)

user = {
  'name' : 'Golem',
  'age' : 5006,
  'can_swin' : False
} # user is an iterable

for item in user: # default it return the dictionery keys.
  print(item)

# different ways to iterate a dictionery
# for item in user.items():
#   print(item) # return an tuple with key values

# for item in user.values():
#   print(item) # return the values of dictionery

# for item in user.keys():
#   print(item) # return the dictionery keys.

# #  iterate key value seperately 
# for key,value in user.items():
#   print(key, value)

# for item in 50:
#   print(item) # TypeError: 'int' object is not iterable, because it a constant value and not a collection thats why it did not iterate

# ----------range() (25/01/2022)----------

# range() it generate a sequence of number using start point to stop point.
# for item in range(0,11):
#   print(item, end=' ')

# ---------enumerate()----------
# using enumerate() function we get the values index(0,'h')

# print(list(enumerate('hello')))
# for index,item in enumerate('hellllllllo'):
#   print(index, item)


# -----------While loops------------
# syntax 
# while conditiom:
  # statement

# Ex
# i = 0
# while i < 10:
#   print(i)
#   i += 1
#   # break
# else:
#   print('loop completed') # else part executed when loop successfuly exited withour breaking the loop

# ---------while loop 2-------
# when should we use while loop & for loop?
# :- when you know how much time you want to iterate a loop then that time use For loop
# for i range(1,5): this runs exactly 4 time
# but you don't have clear idea of how much time to run loop then use while loop
# ex
# while True: # it generate a infinite loop
#   response = input('say something: ')
#   if response == 'bye':
#     break

# ------------Break, Continue, Pass(26/01/2022)----------
# break, Continue and pass this three are the keywords(reserved words) in Python
# what they do?
# lets go one by one
# 1 ///Break is help to exit the loop explicitly///
# Ex of break
for item in range(1,11):
  print(item)
  break #This prevents the loop from completing, and exits.

# 2 ///Continue is help to go back to loop and it never goes next line until loop end///
# Ex of continue
for item in range(1,4):
  continue # from here it goes back to the above line it never goes to the next line
  print(item)

# 3 ///Pass is just name says pass, it do nothing , it didnt give the error also///
# Ex of pass
for item in range(1,3):
  pass # we use the pass for holding for a second, we say hey man hold on let me think the logic but don't break the code let others work.

# --------Developers fundamental Iv---------
# what is a good code?
# easily readable
# don't have any extra stuff
# predictability
# DRY ( do not repeat yourself )
# Reusable(function)

# --------Function---------
# functions is actually the example of DRY priciple How? it says write the piece of code once and then use it anywhere in programe (Reusability)
# there are two types of Functions
# 1 Built in functions & User defined functions
# earlier we the built in functions len(), max(), print(), input() etc.
# user defined function is the who make by Developer.and use it throughout the programe in multiple time

# Syntax (user_defined_fun)
def user_defined_fun(): # its a defining a function, here interpreter says ok i store this function in memory whenever you need this function let me know. 
  print('Hellllllllooooooooooooo')

# user_defined_fun() #its calling the function, here we ask interpreter hey give me the function,in return it gives the function.

# -------parameters and arguments-----------
# what are those?
# parameter is just like we tell function on defining time hey man in future i am sending you some data for some calculation so please accept and use it on function, parameter is initialize on time of the definition of function.
def greet(name):# name in here is we provide the parameter
  print(name)

# Arguments is just like parameter but the argument use when we call the function
# greet('ashwin') # here we sending the argument(real data to the parameter) 
# so parameter is work like a variable and argument is like we assign some data to the variable,like that.
# sometimes we say invoke a function its nothing but a calling a function.


# -------default parameter and keyword argument------

# 1 position argument 
# positional argument says send the data to parameter in a proper order
# Ex
def say_hello(name,emoji):
  print(f'my name is {name}, {emoji}')

# say_hello('🎃','ashwin') # in here we send the emoji to the name variable and actual name send to the emoji variable. so programe is not smart enough to understand which variable need to take which value, so be cautious here #positional argument

# 2 keyword argument
# keyword argument says send the data with the variable name that way you dont confuse which data you are sending to which variable.

say_hello(emoji = '🎃', name='ashwin') # here function get the right value with the wrong positioning of values

# 3 default parameters
# default parameters is just set the default values to the function, it says set the values for variables on defining time, if someone set the argument then it change to the original value and replace with the newer one but if no one give the argument then it took the default one let see.

def normal_fun(name):
  print(name)

# normal_fun() # this throws error because we bound to send the data to the parameter just like a normal variable works, something you need to give

def default_param(name = ''):
  print('my name', name)

default_param() # if we didnt send the data to the param it didnt throw the error because we set the default value
default_param('ashwin') # if we set the value then it changes the default value with argument

# --------return---------


  