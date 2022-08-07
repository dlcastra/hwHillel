# CALCULATOR
print("instruction:\nSUM is: +\nDIFFERENCE is: -\nMULTIPLICATION is: *\nDIVISION is: /\nEXPONENTIATION is: **")
f_num = input("First number =")
s_num = input("Second number =")
operation = input("Your operation is: ")

try:
    f_num = int(f_num)
    s_num = int(s_num)
    if operation == '+':
        result = f_num + s_num
        # print(result)
    elif operation == '-':
        result = f_num - s_num
        # print(result)
    elif operation == '*':
        result = f_num * s_num
        # print(result)
    elif operation == '/':
        result = f_num / s_num
        # print(result)
    elif operation == '**':
        result = f_num ** s_num
        # print(result)
    else:
        print("Error: An invalid character was entered!")
    print(f'You result = {result}', type(result))

except ZeroDivisionError:
    print('Are you serious?1')

except ValueError:
    f_num = float(f_num)
    s_num = float(s_num)
    if operation == '+':
        result = f_num + s_num
        # print(result)
    elif operation == '-':
        result = f_num - s_num
        # print(result)
    elif operation == '*':
        result = f_num * s_num
        # print(result)
    elif operation == '/':
        result = f_num / s_num
        # print(result)
    elif operation == '**':
        result = f_num ** s_num
        # print(result)
    else:
        print("Error: An invalid character was entered!")
    print(f'You result = {result}', type(result))

