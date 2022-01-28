# Counter
sum = 0
for each in list(range(1,11)):
  sum = sum + each

print(sum)

# enumerate()

# print index number where value is 50.
for index,value in enumerate(list(range(1,100))):
  if value == 50:
    print(index, value)