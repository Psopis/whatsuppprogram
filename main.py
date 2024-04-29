import time

from change_mode import make_mode
from file_send import file_sender
from forbidden_nums import already_sent_nums
from message_send import message_sender, get_message_from_file
from getnumbers import create_file_with_numbers, check_file_update


def check_api():
    check_file_update()


def start():
    variation = input("режим работы")
    make_mode(variation)

    # check_file_update()
    # create_file_with_numbers()
    # 89095001418
    # +79059824823
    # +79635379097

    # message_sender("89095001418")
    # file_sender()

    pass


if __name__ == '__main__':
    start()
