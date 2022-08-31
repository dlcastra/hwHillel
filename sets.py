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


# union - union of elements of all sets
first_set = {'1', '2', '3', '4', '5',16}
second_set = {'2', '4', '6', '8', '10', '12',16}
third_set = {0,11,13,15,16}

first_set |= second_set | third_set

# intersection - set of elements that are in each of the sets
first_set1 = {'1', '2', '3', '4', '5',16}
second_set2 = {'2', '4', '6', '8', '10', '12',16}
third_set3 = {0,11,13,15,16}

first_set1 &= second_set2 & third_set3

# difference - the set of elements from set that are not in any other
first_set1a = {'1', '2', '3', '4', '5',16}
second_set2b = {'2', '4', '6', '8', '10',"d", '12',16}
third_set3c = {0,11,13,15,16, "g"}

first_set1a -= second_set2b - third_set3c

# symmetric_difference - the set of elements unique to all sets
first_set1a1 = {'1', '2', '3', '4', '5',16}
second_set2b2 = {'2', '4', '6', '8', '10',"d", '12',16}
third_set3c3 = {0,11,13,15,16, "g"}

first_set1a1 ^= second_set2b2 ^ third_set3c3

print(first_set)
print(first_set1)
print(first_set1a)
print(first_set1a1)
