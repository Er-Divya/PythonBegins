# This program will show how to write list of lists and how to access it's data

list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(list_of_lists[0][2])

# Converting a one dimensional list into a two dimensional list

one_dim_list = ['One', 'dimension', 'list']

# First Approach: Using split method. Split method returns list in string format. This will not work on int data type.


def make_list_two_dimensional(list_passed):
    two_dim_list = []
    for ele in list_passed:
        val = ele.split(' ')
        two_dim_list.append(val)
    print(two_dim_list)


make_list_two_dimensional(one_dim_list)

# Second Approach: Using List comprehension. This approach can be used on int data type values in list as well.
# Syntax for list comprehension is [expression for item in list]


def get_two_dim_list(one_d_list):
    return [[el] for el in one_dim_list]


print(get_two_dim_list(one_dim_list))

# Third Approach: Using python map function


def convert_list_into_two_dim_list(one_dimension_list):
    return list(map(lambda el: [el], one_dimension_list))


print(convert_list_into_two_dim_list(one_dim_list))

