import pywhatkit
import time

from file_send import f
from getnumbers import create_file_with_numbers, check_file_update


def check_api():
    const = check_file_update()


def send_messages(number, message):
    # pywhatkit.sendwhatmsg_instantly(number,message)
    print(number, message)


def start():
    check_api()
    create_file_with_numbers()
    f()


if __name__ == '__main__':
    start()
