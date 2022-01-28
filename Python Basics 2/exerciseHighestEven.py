# create a function highest even and it take a list and give the output the highest even nmber from that list


# 1 iterate the list 
  # check the even number
  # compare the even number to the previous even number
  # return the highest even number

def highest_even(list):
  evenNums = []
  for item in list:
    if item % 2 == 0:
      evenNums.append(item)
  return max(evenNums)

print(highest_even([1,2,3,4,5,6,7,8,9,10,11]))