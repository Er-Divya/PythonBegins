# This program will demonstrate how to use dictionary in python

my_dictionary = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Get specific value from a dictionary. In case specified key not found an error will be thrown.
print(my_dictionary["Sep"])
# Get specific value from a dictionary using get function. If this key not found no error will be thrown.
print(my_dictionary.get("Mar"))
# Try finding finding a key which is not present in dictionary
print(my_dictionary.get("Lov"))
# Show a message in case key not found.
print(my_dictionary.get("loV", "Key not found."))

# For loop on dictionary
print("-----------------Printing key values-----------------------")
for x in my_dictionary:
    print(x)

print("-----------------Printing values--------------------------")
for x in my_dictionary.values():
    print(x)
