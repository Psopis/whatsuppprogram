def check_registration(number):
    file = open("numbers_directory/not_found.txt", "w")
    file_read = open("numbers_directory/not_found.txt", "r").read()
    file_read = set(file_read.split(';'))
    file.write(f"{file_read.add(number)};")
    file.close()
