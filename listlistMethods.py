# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# # access the oranges from list

# print(basket[1][1][0])

# ----------List methods-------------
# # using this list, 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];



# # 1. Remove the Banana from the list
# basket.remove('Banana')

# # 2. Remove "Blueberries" from the list.
# basket.pop()
# # 3. Put "Kiwi" at the end of the list.
# basket.append('Kiwi')
# # 4. Add "Apples" at the beginning of the list
# basket.insert(0,'Apples')
# # 5. Count how many apples in the basket
# print(basket.count('Apples'))
# # 6. empty the basket
# basket.clear()
# print(basket)

# --------------Common list patterns-------------
#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

print(sorted(friends + new_friend))
# friends.extend(new_friend)
# friends.sort()
# print(friends)
# other solution
# friends.extend(new_friend)
# print(sorted(friends))
