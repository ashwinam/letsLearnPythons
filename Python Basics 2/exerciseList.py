# check for duplicates in list and insert into another list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# 1 create a blank list[done]
# 2 iterate over some_list
  # i) set count method on a each item and say if count > 1 append item on list


duplicate = []
for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicate: # make a unique 
      duplicate.append(item)

print(duplicate)

# duplicate = []
# for item in some_list:
#   if item not in duplicate: # make a unique 
#     duplicate.append(item)

# print(duplicate)