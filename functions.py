#################
### First task ##
#################

def get_sum(start, end):
    if start > end:
        start_2 = end
        end = start
        values = sum(range(start_2, end + 1))
    else:
        values = sum(range(start, end + 1))
    return values

print(get_sum(3,67))
print(get_sum(67,3))

##################
### Second task ##
##################

def seconds_conversion(user_time):

    days = user_time // (24 * 60 * 60)
    user_time %= (24 * 60 * 60)

    hours = user_time // (60 * 60)
    user_time %= (60 * 60)

    minutes = user_time // 60
    user_time %= 60

    seconds = user_time

    print(f"Days: {days}\nHours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}")

times = int(input("Enter number in seconds"))
seconds_conversion(times)

############################
### Task three, point one ##
############################

### first version ###

def sum_list(user_number):

    sum_numbers = 0
    words_and_numbers = []

    for element in user_number:

        if isinstance(element, int):
            sum_numbers += element

        elif isinstance(element, str):

            if element.isdigit():
                new_num = int(element)
                sum_numbers += new_num

            if element.isalpha():
                words_and_numbers.append(element)

    print(words_and_numbers)
    return sum_numbers

print(sum_list([1,2,3,'4','ksdjk']))

i = input('Your list: ').split()
print(sum_list(i))

### Second version ###

def get_sum_list(user_number):

    sum_numbers = 0

    for element in user_number:

        if isinstance(element, int):
            sum_numbers += element

        elif isinstance(element, str):

            new_num = int(element)
            sum_numbers += new_num

    return sum_numbers
print(get_sum_list([1,2,3,'4']))

i = input('Your list: ')
print(get_sum_list(i))

############################
### Task three, point two ##
############################

def while_sum_list(user_list):

    list_length = len(user_list)
    sum_numbers = 0
    count = 0

    while count < list_length:
        sum_numbers = sum_numbers + user_list[count]
        count = count + 1

    return sum_numbers

print(while_sum_list([1,2,3,34,5,6,7]))

#############################
## Task three, point three ##
#############################

def recursion_sum_list(user_list):

    if user_list == []:
        return 0

    else:
        return user_list[0] + recursion_sum_list(user_list[1:])

print(recursion_sum_list([1,2,3,34,5,6,7]))

######################
## Task number four ##
######################

def fib(n):

    if n <= 1:
        return n

    else:
        return fib(n - 1) + fib(n - 2)

print(fib(20))

######################
## Task number five ##
######################

def first_layer(ingredients):

    print("Ingredients for a sandwich\n")
    print("Tomato")

    return ingredients


@first_layer
def second_layer(ingredients):

    print("Meat")

    return ingredients


@second_layer
def third_layer(ingredients):

    print("Cheese")

    return ingredients


@third_layer
def four_layer(ingredients):

    print("Bread\n")
    print("Sandwich is ready")

    return ingredients


@four_layer
def sandwich(ingredients):

    return ingredients

