from selenium import webdriver
from selenium.webdriver import Keys # klaviaturada knopka bosih imitatsiya qilish uchun
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # find_element ishlatish uchun shuni import qilish kerak
import time
from auth_data import mail_password
import random

url = 'https://account.mail.ru/login'

# options
options = webdriver.ChromeOptions()

# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\automate_smartup\\chromedriver.exe")

# drayeverga adresni korsatishda 1 ta teskari slesh ishlatmoqchi bolsa 'r' (экранирование)
# dan foydalanish kerak
# r"D:\GitHubRepos\automate_smartup\chromedriver.exe"

options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1')

driver = webdriver.Chrome(
    service=service,
    options=options
    )

try:
    driver.get(url)
    time.sleep(3)
    email_input = driver.find_element(By.NAME, 'username')
    email_input.clear() # biror matn kiritilgan bo'lsa tozalavoradi
    email_input.send_keys('reg.1@bk.ru')
    time.sleep(3)

    '''
    Knopka bosihni 2 usuli bor
    1. Enter knopka bosihni imitatsiya qilish - send_keys(Keys.ENTER)
    2. Sichqoncha bilan bosishni imitatsiya qilish - click()
    
    CSS_SELECTOR orqali izlaganda barcha css selektorlar nuqta bilan boshlanishi kerak va ular ko'p bolsa orasida probel bo'lmasligi kerak
    '''
    # password_input = email_input.send_keys(Keys.ENTER)

    # CSS_SELECTOR orqali izlaganda barcha css selektorlar nuqta bilan boshlanishi kerak va ular ko'p bolsa orasida probel bo'lmasligi kerak
    password_button = driver.find_element(By.CSS_SELECTOR, '.base-0-2-87.primary-0-2-101.auto-0-2-113')
    password_button.click()
    time.sleep(3)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(mail_password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
