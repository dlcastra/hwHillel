################
## First task ##
################

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

#################
## Second task ##
#################

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

###########################
## Task three, point one ##
###########################

def all_even_and_odd(user_number): # all even and odd numbers from 0 to "user_number"

    even_numbers = ''
    odd_numbers = ''

    for number in range(user_number):

        if number % 2 == 0:

            even_numbers += str(number) + "; "
        else:
            odd_numbers += str(number) + "; "

    print(f"It is your even numbers: {even_numbers}\nIt is your odd numbers: {odd_numbers}")

## Exemple

# all_even_and_odd(12)
# It is your even numbers: 0; 2; 4; 6; 8; 10;
# It is your odd numbers: 1; 3; 5; 7; 9; 11;

some_numbers = int(input("Enter numbers: "))
operation = all_even_and_odd(some_numbers)

###########################
## Task three, point two ##
###########################

def password(user_password):

    library = user_password
    counter = 0

    while 1:

        user_password = input("Enter your password if you want open this page: ")
        if user_password != library:

            counter += 1

            if counter < 3:
                print("Try again")

            if counter == 3:
                print("Page is blocked")
                break

        if user_password == library:
            print("Well done")
            break

op = input("Create your password: ")
password(op)


def check_password(user_password):

    first_input = user_password
    library = first_input


    while 1:

        user_password = input("Enter the password a second time: ")
        if user_password != library:
            print("Try again")

        if user_password == library:
            print("Well done")
            break

operation_1 = input("Create your password: ")
check_password(operation_1)
