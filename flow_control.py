# CALCULATOR
print("instruction:\nSUM is: +\nDIFFERENCE is: -\nMULTIPLICATION is: *\nDIVISION is: /\nEXPONENTIATION is: **")
first_num = input("First number =")
second_num = input("Second number =")
operation = input("Your operation is: ")
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

    print(f"Your result = {result}")
# block error
except ZeroDivisionError:
    print('Are you serious??!')

except Exception as error:
    print("Please don't use alphabet")
