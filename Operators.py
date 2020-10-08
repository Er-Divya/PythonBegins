# This program demonstrate few of the mathematical operators in python

# Python Arithmetic Operators
first_num = 70
second_num = 10

print("Addition operator: " + str(first_num + second_num))
print("Subtraction operator: " + str(first_num - second_num))
print("Multiplication operator: " + str(first_num * second_num))
print("Division operator: " + str(first_num / second_num))
print("Modulus operator: " + str(first_num % second_num))

# Python Assignment Operators
new_num = first_num
print("New number is: " + str(new_num))
new_num += 1
print("Incremented value of new number: " + str(new_num))
new_num -= 4
print("Decremented value of new number: " + str(new_num))

# Python Comparision Operators
com_num_first = 22
com_num_second = 24

if com_num_first == com_num_second:
    print("Awesome! Numbers are equal.")
elif com_num_first > com_num_second:
    print("First number is greater than second number.")
else:
    print("Second number is greater than the first number.")

# Python Logical Operators
is_tall = False
is_male = False

if is_tall and is_male:
    print("You are a tall male.")
elif is_tall and not is_male:
    print("You are tall but not male.")
elif not is_tall and is_male:
    print("You are a short male.")
else:
    print("You are neither tall nor male.")