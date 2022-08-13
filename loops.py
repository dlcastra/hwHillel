
something_latter = input('input something:')
capital_letters = ""
spaces = ""
vowels_list = ""
counter = 0

for index, letter in enumerate(something_latter):

    if letter.isupper():
        capital_letters += letter

    if letter == " ":
        spaces += str(index, ) + "; "

    if letter.lower() in 'a e i o u':
        vowels_list += letter

    if letter.isdigit():
        counter += 1

        if counter == 3:
            print("Sorry, but you have too many numbers in a row")
            break
        if letter == str():
            counter = 0
            continue

if counter != 3:
    print(capital_letters)
    print(spaces)
    print(vowels_list)
    print('Correct end of the cycle')
