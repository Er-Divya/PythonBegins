# Lopping over a list

names = ['Kerry', 'Kaali', 'Neel', 'Nitin', 'Mukesh']

index = 1
for name in names:
    print(index, name)
    index += 1

print("----------------------------------------------")
# Above looping can be done using enumerator method provided in python

places = ['Eta', 'Kan', 'Luck', 'Gwal', 'Noida']

for index, name in enumerate(names, start=1):
    print(index, name)

