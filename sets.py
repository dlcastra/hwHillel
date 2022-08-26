# First task
#
first_set = input("Input something")
second_set = input("Input something")

found_numbers = set(first_set).symmetric_difference(second_set)
found_letters = set(first_set).intersection(second_set)

operation_with_digits = {el for el in found_numbers if el.isdigit()}
operation_with_letters = {el for el in found_letters if el.isalpha()}

print(list(operation_with_digits))
print(list(operation_with_letters))

# Second task

first_set = {'1', '2', '3', '4', '5',16}
second_set = {'2', '4', '6', '8', '10', '12',16}
third_set = {0,11,13,15,16}
# first_set = {1, 2, 3, 4, 5, 16}
# second_set = {2, 4, 6, 8, 10, 12, 16}
# third_set = {0, 11, 13, 15, 16,}

first_set |= second_set | third_set
second_set &= first_set & third_set
third_set -= second_set - third_set
op = first_set ^ second_set ^ third_set

print(first_set)
print(second_set)
print(third_set)
print(op)