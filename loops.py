something_latter = input('input something:')

capital_letters = ""
spaces = ""
vowels_list = ""
counter = 0

for index, letter in enumerate(something_latter):

    if letter.isupper():
        capital_letters += letter

    if letter == " ":
        spaces += str(index) + ";"

    if letter.lower() in 'aeiouAUIOE':
        vowels_list += letter

    if letter.isdigit():
        counter += 1
        if counter == 3:
            print("Sorry, but you have too many numbers in a row\n")
            break
    else:
        counter = 0

print(f"Letter ir high register capital letters = {capital_letters}\n")
print(f"All whitespace indexes spaces = {spaces}\n")
print(f"All vowels vowels_list = {vowels_list}\n")
print('Correct end of the cycle')
