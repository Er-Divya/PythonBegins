# UnPacking

items = [1, 2, 3, 4, 5, 6, 7]
print(items)

# Below code will unpack first element of list in a and rest will be ignored.
a, _ = [3, 4]
print(a)

# First two elements of the list will be unpacked and stored in x and y. Rest all will be stored in z
x, y, *z = [10, 11, 12, 13, 14, 15, 16, 17, 18]
print("Printing value of x, y and z: ")
print(z)
print(y)
print(z)
