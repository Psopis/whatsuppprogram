import json
import os
import time
from itertools import chain

import pyautogui
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from forbidden_nums import forbiden_nums, already_sent_nums
from getnumbers import create_file_with_numbers
from log_add import log_add_text
from non_register_nums import check_registration


def profile_make():
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(
        r'user-data-dir=\profiles')  # УКАЖИТЕ ПУТЬ ГДЕ ЛЕЖИТ ВАШ ФАЙЛ. Советую создать отдельную папку.
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument('--profiling-flush=n')
    options.add_argument('--enable-aggressive-domstorage-flushing')
    return options


def get_message_from_file(file_name):
    # create_file_with_numbers()

    file = open(f"numbers_directory/{file_name}", "r").read()

    message = open("files/message_for_users.txt", "r", encoding='utf-8').read()
    alredy_sents = open("numbers_directory/already_sent.txt", "w")

    js = json.loads(file)

    for i in js:
        print(i)
        if forbiden_nums(i['phone']) != False:
            if already_sent_nums(i['phone']):
                print(123)
                pass
            else:
                msg = message.format(i['link'], encoding='utf-8')

                message_sender(i['phone'], msg, i)

                log_add_text(message=msg, number=i['phone'])

    alredy_sents.write(f"{js}")
    alredy_sents.close()


def message_sender(number, message, js):
    driver = webdriver.Chrome(options=profile_make())
    wait = WebDriverWait(driver, 30)

    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(url)

    element_of_non_registr = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[1]")))
    if element_of_non_registr.text != 'Начало чата':
        check_registration(js)
    else:

        # ДОДЕЛАТЬ
        # ДОДЕЛАТЬ
        # ДОДЕЛАТЬ
        xpath_prefix = "/html/body/div[1]/div/div/div[2]/div[4]/div/div[3]/div/div[2]"

        dom = etree.HTML(driver.page_source)

        table_headers = dom.xpath(xpath_prefix)

        for i in table_headers:
            pass
        # print(str(etree.tostring(i)))
        # ДОДЕЛАТЬ
        # ДОДЕЛАТЬ
        # ДОДЕЛАТЬ
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

    # if message_check != '' or aponent_message_check != '':
    #     pass

    files = os.listdir('attachments')

    if files:
        btn = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div"))
        )
        btn.click()
        upload_box = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[1]/li"))
        )
        upload_box.click()
        time.sleep(.5)
        pyautogui.write(os.getcwd() + fr'\attachments\{files[0]}')
        pyautogui.press('enter')
        wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div"))
        ).click()
        time.sleep(5)
