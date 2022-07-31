user_name = str(input("Hi, tell mi your name:"))
removing_spaces = user_name.strip()
correct_reg = removing_spaces.capitalize()
greetings = f"Hi {correct_reg}, you are so cool"
nb_in_name = len(correct_reg)

print(greetings)
print("See how i can")
print("Your name consists of",nb_in_name,"letters")
print("I swap your name:", correct_reg[::-1])
