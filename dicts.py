import string
# First task

dictionary_generator = {element: chr(element) for element in range(128)}
print(dictionary_generator)

# Second task

user_message = input("Input your message: ")
step = int(input("Input password: "))
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


def methods_and_functions():
    new_dict = {
        "color1": "Red",
        "color2": "Blue",
        "color3": "Yellow",
        "number": 1
    }

    keys = new_dict.keys()  # Метод keys() вернет список всех ключей в словаре
    values = new_dict.values()  # Метод values() вернет список всех значений в словаре.
    items = new_dict.items()  # Метод items() возвращает каждый элемент словаря в виде кортежей в списке.
    color = new_dict.get("color1")  # Показать елемент по ключу

    print(f"\nBefore changes\nDict {new_dict}")
    print(f"All keys is {keys}")
    print(f"All values is {values}")
    print(f"All items is {items}")
    print(color)

    new_dict["number2", "number3"] = "2", "3"
    new_dict["some_car"] = "Ford"  # Добавляет новый ключ и элемент если подобных ключей не существует
    new_dict["color1"] = "Green"  # Меняет елемент по ключу
    new_dict.update({"color2": "Black"})  # Меняет елемент по ключу
    new_dict.update({"color4": "Purple"})  # Добавляет новый ключ и элемент если подобных ключей не существует
    new_dict.pop(("number2", "number3"))  # Метод pop() удаляет элемент с указанным именем ключа
    new_dict.popitem()  # Метод popitem() удаляет последний вставленный элемент
    del new_dict[
        "number"]  # Ключевое слово del удаляет элемент с указанным именем ключа, del также может полностью удалить словарь
    # new_dict.clear() # Метод clear() очищает словарь

    print(f"\nAfter changes\nDict {new_dict}")
    print(f"All keys is {keys}")
    print(f"All values is {values}")
    print(f"All items is {items}")

    if "color1" in new_dict:
        print(new_dict["color1"])

    x = ('key1', 'key2', 'key3', 'key4')  # Создает словарь со значениями которые == у
    y = 5  # По умолчанию всегда 0
    thisdict = dict.fromkeys(x, y)
    print(thisdict)

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.setdefault("color", "white")  # Получить значение элемента «цвет», если элемента «цвет» не существует, вставить «цвет» со значением «белый»
    print(f"Car color is {x}")


# methods_and_functions()


def loop_dictionaries():
    new_dict = {
        "color1": "Red",
        "color2": "Blue",
        "color3": "Yellow",
        "number": "1"
    }

    for i in new_dict:  # Вывод всех ключей словаря
        print(i)

    for i in new_dict.keys():  # Вывод всех ключей словаря
        print(i)

    for i in new_dict:  # Все значения в словаре, одно за другим
        print(new_dict[i])

    for i in new_dict.values():  # Все значения в словаре, одно за другим
        print(i)

    for i, j in new_dict.items():  # Вывод ключей и значений с помощью метода items()
        print(i, j)


# loop_dictionaries()


def dictionary_copying():
    new_dict = {
        "color1": "Red",
        "color2": "Blue",
        "color3": "Yellow",
        "number": "1"
    }

    copy_dict = new_dict.copy()  # Сделать копию словаря
    copy_dict1 = dict(new_dict)  # Сделать копию словаря

    print(copy_dict)
    print(copy_dict1)


# dictionary_copying()


def nested_dictionaries():
    my_children = {
        "child1": {
            "name": "Emil",
            "year": 2004,
            "height": 180,
            "weight": 70
        },

        "child2": {
            "name": "Tobias",
            "year": 2007,
            "height": 170,
            "weight": 60
        },

        "child3": {
            "name": "Linus",
            "year": 2011,
            "height": 110,
            "weight": 40
        }
    }

    for i, j in my_children.items():
        print(i, j)


# nested_dictionaries()