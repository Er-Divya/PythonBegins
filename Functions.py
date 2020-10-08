# This file demonstrate how to write functions in python
# Function without parameter


def say_hi():
    print("Hey there..")


say_hi()

# Function with parameter


def say_hi(name):
    print("Hello " + name)


say_hi("Ram")

# Function with return value


def cube(num):
    return num*num*num


print("Cube of number 8 is " + str(cube(8)))
