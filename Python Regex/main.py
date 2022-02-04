# REGULAR EXPRESSIONS AKA regex
#  regex is very helpful in finding the patterns, patterns like email or password verification

import re
string = 'search inside of this text this please!aaa'
# print('search' in string)  # re is more powerful than this

pattern = re.compile('search inside of this text this please!')
# a = re.search(pattern, string)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# a = pattern.search(string)
# # print(a)
# b = pattern.findall(string)
# print(b)
# # it runs when the pattern == search, it finds eexact match
# c = pattern.fullmatch(string)
# print(c)
# d = pattern.match(string)
# print(d)

# email validator
emailValidator = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
emailAddr = 'name@name.com'
print(emailValidator.findall(emailAddr))

# Password validator
'''
conditions
1. At least 8 character long
2. contain any sort letters, numbers $#%@
3. end with numbers
'''
passwordValidator = re.compile(r'([A-Za-z0-9$%#@]{7,}[0-9])')
password = 'ashwin@123'

print(passwordValidator.match(password))
