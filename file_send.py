import os
import pyautogui
from message_send import profile_make
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait


def file_sender(file_path, message, number):
    driver = webdriver.Chrome(options=profile_make())
    wait = WebDriverWait(driver, 30)

    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(url)
    btn = WebDriverWait(driver, 60).until(
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
    pyautogui.write(os.getcwd() + file_path)
    pyautogui.press('enter')
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div"))
    ).click()
    time.sleep(5)
