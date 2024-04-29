import json


def forbiden_nums(number):
    file = open("numbers_directory/forbidden.txt", "r").read().replace(' ', '').split(',')

    for j in file:
        if j == number:
            print("bad phone ", number)
            return False


def already_sent_nums(number):
    file = open("numbers_directory/already_sent.txt", "r").read()
    print(file)
    if file == '':
        file_add = open("numbers_directory/already_sent.txt", "w").write('[]')

    f = json.loads(file.replace("'", '"'))
    print(f)
    for i in f:
        if i['phone'] == number:
            return False
