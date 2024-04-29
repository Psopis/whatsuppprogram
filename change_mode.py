import time

from getnumbers import create_file_with_numbers
from message_send import get_message_from_file


def make_mode(mode):
    if mode == '1':
        while (True):
            time.sleep(3)
            create_file_with_numbers()
            get_message_from_file("numbers.txt")
    elif mode == '2':
        get_message_from_file("not_found.txt")
    elif mode == '3':
        get_message_from_file("already_sent.txt")
    else:
        return False
