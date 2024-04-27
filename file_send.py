import time


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=files/asd.txt') # УКАЖИТЕ ПУТЬ ГДЕ ЛЕЖИТ ВАШ ФАЙЛ. Советую создать отдельную папку.
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--profiling-flush=n')
options.add_argument('--enable-aggressive-domstorage-flushing')

def f():
    driver = webdriver.Chrome( options=options)
    wait = WebDriverWait(driver, 30)

    numbers = ["+79609398702", "+70000000001"]
    text = "Привет+мир!"

    for number in numbers:
        url = f"https://web.whatsapp.com/send?phone={number}&text={text}"
        driver.get(url)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        time.sleep(5)