### Error in Python

# Error is Errors, We always see the errors, when we write wrong syntax, do something else that interpreter doesn’t understand that time it shows a message that say hey you did something wrong I shut down the programme, in simple words due to errors our programe is crashed.

# **Types Of Errors In Python**
# Lets see few of them

# - SyntaxError
# - NameError
# - IndexError
# - TypeError
# - KeyError
# - ZeroDivisionError

# [Built-in Exceptions - Python 3.10.2 documentation](https://docs.python.org/3/library/exceptions.html)

# **How Do We avoid Errors?**

# Programmes are constantly accessed by outside entity, Input are get by the users are uncertain it throws anything towards programe, so that way there is the possibility that programme is crashed, for that we have the Error Handling for prevent this type of accidents.

# ------------Error Handling in Python------------------
# while True:
#     try:
#         age = int(input('what is your age? '))
#         # when i give the string it shows me error, and it crashed so how to avoid this? Error Handling
#         10/age
#     except ZeroDivisionError as Err:
#         print('Please Enter a Number that is more than 0', Err)
#     except ValueError as Err:  # here Err work as a variable that store ValueError Error
#         print('Please Enter a Number', Err)
#     else:  # else part is executed when there is no errors
#         print('Thank You!')
#         break

# That way we can Handle varrious type of error, each input error give different message
# 1. Add multiple Except statement for various errors.
# 2. Except statement only works one time, if the except hit by error so it executed one time and it goes in while statement.

# -----------------Error Handling 2------------------


def sums(num1, num2):
    try:
        return num1 + num2
    except TypeError as Err:
        return 'Please Enter a Number'
    except (TypeError, ZeroDivisionError) as Err:  # we will write this also
        pass


# print(sums(1, 2))

# ---------Exercise: Error Handling----------------

# while True:
#     try:
#         age = int(input('what is your age? '))
#         # when i give the string it shows me error, and it crashed so how to avoid this? Error Handling
#         10/age
#     except ZeroDivisionError as Err:
#         print('Please Enter a Number that is more than 0', Err)
#         continue
#     except ValueError as Err:  # here Err work as a variable that store ValueError Error
#         print('Please Enter a Number', Err)
#         break
#     else:  # else part is executed when there is no errors
#         print('Thank You!')
#         break
#     finally:
#         print('Finaly I am Executed :)')
#     print('Can you hear me?')


# --------------Error Handling 3---------------
# Sometimes we want the programe need to be stop working at a certain situation for that sitatio we need to raise an error, so python has a raise function to raise an error


while True:
    try:
        age = int(input('what is your age? '))
        # when i give the string it shows me error, and it crashed so how to avoid this? Error Handling
        10/age
        # raise ValueError('Stop this thing')
        raise Exception('Stop this thing')
    except ZeroDivisionError as Err:
        print('Please Enter a Number that is more than 0', Err)
    # except ValueError as Err:  # here Err work as a variable that store ValueError Error
    #     print('Please Enter a Number', Err)
        # break
    else:  # else part is executed when there is no errors
        print('Thank You!')
        break
    finally:
        print('Finaly I am Executed :)')
