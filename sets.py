# First task

first_set = input("Input something")
second_set = input("Input something")

found_numbers = set(first_set).symmetric_difference(second_set)
found_letters = set(first_set).intersection(second_set)

operation_with_digits = {el for el in found_numbers if el.isdigit()}
operation_with_letters = {el for el in found_letters if el.isalpha()}

print(list(operation_with_digits))
print(list(operation_with_letters))

# Second task

# first_set = {'1', '2', '3', '4', '5'}
# second_set = {'2', '4', '6', '8', '10', '12'}


