# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('bruno', 2)
cat2 = Cat('simon', 3)
cat3 = Cat('apple', 1)

# print(cat1.age, cat2.age, cat3.age)

# 2 Create a function that finds the oldest cat


def oldest_cat():
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1.age
    elif cat2.age > cat3.age and cat2.age > cat1.age:
        return cat2.age
    else:
        return cat3.age


def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f'the age of oladest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)}')
