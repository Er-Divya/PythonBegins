# This program will demonstrate how we can implement and perform various functions and statements on lists.

lucky_numbers = [4, 84, 15, 12, 23, 42]
friends = ['Joey', 'Monica', 'Rachel', 'Ross', 'Chandler', 'Phoebe']

# Extend Function: Using this function we can add two lists together
friends.extend(lucky_numbers)
print(friends)

# Append Function: Add an item at the end of the list
friends.append(48)
print(friends)

# Insert Function: Add an item at any place in the list
# Below example I am adding an element at the last place
friends.insert(len(friends), "Gunther")
print(friends)

# Inserting an element in the middle of the list
friends.insert(len(friends)-8, "Mike")
print(friends)

# Remove Function: This function removes any specified elements in the list
friends.remove("Gunther")
print(friends)

# Pop function: This function will remove the last item of the list
print(friends.pop())
print(friends)

# Index Function: This function can be used to check if a element exist in the list
# print(friends.index("phoebe")) ---> This will throw error as index function has case sensitive parameter value.
print(friends.index("Phoebe"))

# Count Function: This function will count number of times an item occurred in the list
print(friends.count("Phoebe"))

# Sort Function: This function will sort the list items in ascending order.
# print(friends.sort()) ---> This will through error as string and integer two different data types.
lucky_numbers.sort()
print(lucky_numbers)

# Copy Function: This function will copy list values in another list.
friends_replica = friends.copy()
print(friends_replica)

# Clear Function: Clears whole list
print(friends.clear())

