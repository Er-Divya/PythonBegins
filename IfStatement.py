# This file will demonstrate how to use if statement in python

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not is_tall:
    print("You are a short male.")
elif is_tall and not is_male:
    print("You are tall but not a male.")
else:
    print("You are neither tall nor male.")