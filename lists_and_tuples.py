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

                for element in input_list]

print(f"Change list: {complete_list}")  # [1, 2.1, -1, '6', 9, '3', 18, -1]


def list_items():
    example_list = ["1", "2", "3", "4", "5", "6"]
    example_list1 = [7, 8, 9, 10]
    example_list.insert(0, "0")
    example_list.extend(example_list1)
    example_list.remove(10)
    example_list.pop(9)
    del example_list[1]
    # example_list.clear()

    for i in range(len(example_list)):
        print(example_list[i])

    # [print(x) for x in example_list]

    new_num_list = [number if type(number) == int and number % 2 == 0
                    else int(number) if type(number) == str and int(number) % 2 == 0
                    else 0
                    for number in example_list]

    new_num_list.sort()
    # new_num_list.sort(reverse=True)
    zero_counter = new_num_list.count(0)
    print(new_num_list, f"{zero_counter} zeros are on the list")


list_items()
