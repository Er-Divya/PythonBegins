# This program will demonstrate try catch in python

# Broad Range of exception

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid input")

# Printing the exact exception

try:
    num = int(input("Enter another number: "))
    print(num % 0)
except Exception as ex:
    print(ex)

# Catching specific exceptions

try:
    user_input = int(input("Enter a number: "))
    value = 10/0
    print(value)
except ZeroDivisionError:
    print("Invalid division: A number should not be divided by 0.")
except ValueError:
    print("Invalid input: Expected input should be an integer.")
finally:
    print("Work done!")
