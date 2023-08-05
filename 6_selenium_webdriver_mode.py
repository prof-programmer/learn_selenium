from selenium import webdriver
from selenium.webdriver import Keys  # klaviaturada knopka bosih imitatsiya qilish uchun
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # find_element ishlatish uchun shuni import qilish kerak
import time

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

# options
options = webdriver.ChromeOptions()

# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\learn_selenium\\chromedriver.exe")

# drayeverga adresni korsatishda 1 ta teskari slesh ishlatmoqchi bolsa 'r' (экранирование)
# dan foydalanish kerak
# r"D:\GitHubRepos\automate_smartup\chromedriver.exe"

options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1')

# disable webdriver mode

'''
for older ChromeDriver under version 79.0.3945.16
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
'''

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    service=service,
    options=options
)

try:
    driver.get(url)
    time.sleep(5)

    driver.save_screenshot('webdriver_mode_off.png')
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
