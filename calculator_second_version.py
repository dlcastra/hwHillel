
print("instruction:\nSUM is: +\nDIFFERENCE is: -\nMULTIPLICATION is: *\nDIVISION is: /\nEXPONENTIATION is: **")
print("If you want to exit the program enter: exit ")

while True:

    first_num = input("First number =",)
    if first_num == "exit":
        break
    second_num = input("\nSecond number =")
    if second_num == "exit":
        break
    operation = input("\nYour operation is: ")
    if operation == "exit":
        break
    result = 0

    try:
        operand_1 = int(first_num) if first_num.isdigit() else float(first_num)
        operand_2 = int(second_num) if second_num.isdigit() else float(second_num)

        if operation == "+":
            result = operand_1 + operand_2

        elif operation == "-":
            result = operand_1 - operand_2

        elif operation == "*":
            result = operand_1 * operand_2

        elif operation == "/":
            result = operand_1 / operand_2

        elif operation == "**":
            result = operand_1 ** operand_2
        else:
            print("Error: An invalid character was entered!")

        print(f"Your result = {result}\n")
    # block error
    except ZeroDivisionError:
        print('Are you serious??!')

    except Exception as error:
        print("Please don't use alphabet")