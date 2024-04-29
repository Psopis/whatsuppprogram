import requests
import json


def get_numbers():
    # response = requests.get("https://vmi458761.contaboserver.net/rept?token=ac7fa63332a1c87238af2cad5e8beae5")

    return open("numbers_directory/nums.txt", "r").read()


def get_text_from_msgfile():
    file = open("files/message_for_users.txt", "r").read()
    return file


def create_file_with_numbers():
    file = open("numbers_directory/numbers.txt", "w")
    response = get_numbers()
    print(response)
    file.write(f"{get_numbers()}")
    file.close()


def add_new_phone(response):
    file = open("numbers_directory/numbers.txt", "w")
    file.write(f"{response}")
    file.close()


def create_array_fromjson(response):
    new = []
    for i in response:
        new.append(i['phone'])
    return new


def check_file_update():
    file = open("numbers_directory/numbers.txt", "r").read()
    dict_main_file = json.loads(file)
    dict_response = json.loads(get_numbers())

    if len(dict_main_file) < len(dict_response):
        add_new_phone(dict_response)

