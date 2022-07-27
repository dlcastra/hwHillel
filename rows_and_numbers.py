# head a program

user_name = input("Tell mi your name. I'm:")
greetings = f"Hi {user_name}! I want to surprise you! :D"
f_nb = float(input("What is you favorite number? \nMy favorite number is:"))

# simple math

f_nb_non_flt = int(f_nb)
degree = f_nb_non_flt ** 4
sq_root = f_nb_non_flt * 0.5
rmdr = f_nb_non_flt % 2

print(greetings)
print(f_nb)
print(f_nb_non_flt)
print(degree)
print(sq_root)
print(rmdr)
print("This is your number in different digits")