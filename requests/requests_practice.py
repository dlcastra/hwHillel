import requests
import json

# Task 4.1

url = "https://jsonplaceholder.typicode.com/posts/1"


def saving_in_json():
    reading = requests.get(url)
    save_data = reading.json()

    with open('request.json', 'w') as save_in_json:
        json.dump(save_data, save_in_json, indent=4)

    print(f"{reading.status_code = }")
    print(f"{save_data = }\n")


saving_in_json()


# Task 4.2

def read_and_save():
    with open('request.json', 'r') as read_and_save_json:
        response_data = json.load(read_and_save_json)

        put = requests.put(url, data=response_data)

    print(f'{response_data = }')
    print(f'{put.status_code = }\n')


read_and_save()
# Task 4.3

some_url = 'https://stackoverflow.com/'


########################################################################################################################

def html_code():
    query = requests.get(some_url)
    change_type = query.text

    with open('query.url', 'w', encoding='utf-8') as url_code:
        url_code.write(change_type)


html_code()


########################################################################################################################

def encod_type():
    query_1 = requests.get(some_url)
    encoding_type = query_1.encoding
    print(encoding_type)


encod_type()


########################################################################################################################

# Task 5

def download_pic():
    picture = requests.get("https://moya-planeta.ru/upload/images/xl/c2/11/c2118c599348f3ce7bbcfe5e9696a0bb.jpg")

    with open('photo.jpg', 'wb') as sunset:
        sunset.write(picture.content)


download_pic()
