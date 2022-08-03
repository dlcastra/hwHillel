print("instruction:\nSUM is: +\nDIFFERENCE is: -\nMULTIPLICATION is: *\nDIVISION is: /\nEXPONENTIATION is: **")

operation = input("Your operation is: ")
f_num = float(input("First number ="))
s_num = float(input("Second number ="))

if operation == '+':
    result = f_num + s_num
    print("Result =", result)

elif operation == '-':
    result = f_num - s_num
    print("Result =", result)

elif operation == '*':
    result = f_num * s_num
    print("Result =", result)

elif operation == '/':
    result = f_num / s_num
    print("Result =", result)

elif operation == '**':
    result = f_num ** s_num
    print("Result =", result)

else:
    print(f"Error: An invalid character was entered!")