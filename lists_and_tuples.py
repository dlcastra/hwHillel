# First task

value = input("Input your sentence").split()

print(value[2::3])

# Second task

input_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]

complete_list = [element if type(element) == float

            else element if (type(element) == int and element % 2 == 0)

            else element ** 2 if (type(element) == int and element % 2 != 0)

            else (str(int(element) * 3)) if (type(element) == str and element.isdigit())

            else -1

            for element in input_list

]

print(f"Change list: {complete_list}")  # [1, 2.1, -1, '6', 9, '3', 18, -1]

