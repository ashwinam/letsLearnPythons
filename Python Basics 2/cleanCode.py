# lets try clean coding with below problem

# calculate odd or even
# 1 approach
def is_odd_or_even(num):
  if num % 2 == 0:
    return True
  elif num % 2 == 1:
    return False



# lets clean the code
def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False



# lets clean more

def is_even(num):
  if num % 2 == 0:
    return True
  return False

# lets clean more
def is_even(num):
  return num % 2 == 0 # this line return the boolean

print(is_even(50))