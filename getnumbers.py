import requests
import json


def get_numbers():
    # response = requests.get("https://vmi458761.contaboserver.net/rept?token=ac7fa63332a1c87238af2cad5e8beae5")

    return open("nums.txt", "r").read()


def create_file_with_numbers():
    file = open("numbers.txt", "w")
    response = json.loads(get_numbers())
    for i in response:
        file.write(f"{i['phone']}, ")
    file.close()


def add_new_phone(response):
    file = open("numbers.txt", "a")
    print(response)
    for i in response:
        file.write(f"{i}, ")

    file.close()


def create_array_fromjson(response):
    new = []
    for i in response:
        new.append(i['phone'])

    return new


def check_file_update():
    file = open("numbers.txt", "r").read()
    dict_main_file = file.split(', ')
    dict_response = create_array_fromjson(json.loads(get_numbers()))
    new = []
    if len(dict_main_file) < len(dict_response):

        for i in range(len(dict_response), len(dict_main_file)):
            add_new_phone(dict_main_file[i])
            new.append(dict_main_file[i])
            return new
    new = []
