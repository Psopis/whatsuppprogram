from datetime import datetime


def log_add_text(message, number):
    file = open('files/Log_file.txt', 'a')
    datetime.now()

    file.write(f"""
Время - {datetime.now()}
Номер телефона - {number}
Сообщение - {message}
\n""")
    file.close()
