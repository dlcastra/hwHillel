# First task

dictionary_generator = {element : chr(element) for element in range(128)}
print(dictionary_generator)

# Second task

user_message = input("Input your message: ")
step = int(input("Input password: "))

import  string


alphabet_generator = dict(zip(string.ascii_lowercase, range(27)))
new_element = []

for element in user_message:

    if element in alphabet_generator:
        new_position = alphabet_generator[element] + step

        while 1:
            new_position = (int(new_position) - 26) if (int(new_position) > 26) else new_position

            if new_position < 26:
                break
        new_element.append(list(alphabet_generator.keys())[list(alphabet_generator.values()).index(new_position)])

    else:
        new_element.append(element)

print(f'Your cipher: {("".join(new_element))}')


