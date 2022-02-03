# Debugging In python
# Programs are full of Bugs, most of the time we just resolve the bugs
# Bugs: Bugs is a piece of code that dont work
# Debugging code : Finding Bugs and removing the bugs

# There are lots of ways to debug code
# Linting : it gives the signal that you write code wrong before executing , its a editor feature
# IDE / Editor : some IDE have features to debug code easily
# read Error : its the best thing to read errors
# PDB : python debugger, its a built in module(standard library) to hep debug the code

import pdb


def add(n1, n2):
    # print(n1, n2)  # print is a quick and easy way to debug code
    pdb.set_trace()  # https://docs.python.org/3/library/pdb.html
    return n1 + n2


add(1, 2)
