import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"
url2 = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

user_agent_list = [
    'Hello_world',
    'Best_of_the_best',
    'python_where'
]

useragent = UserAgent()

# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\automate_smartup\\chromedriver.exe")

# drayeverga adresni korsatishda 1 ta teskari slesh ishlatmoqchi bolsa 'r' (экранирование) dan foydalanish kerak
# r"D:\GitHubRepos\automate_smartup\chromedriver.exe"

# options
options = selenium.webdriver.ChromeOptions()

'''
chromium optsiyalari ro'yxati - https://peter.sh/experiments/chromium-command-line-switches/
user agent qoyamiz, istalgan user agent qoysa boladi, xohlasak android user agentni kiritsak boladi
options.add_argument('user-agent=HelloWorld')
user-agentga istalgan narsa yozsa boladi, faqat chegarani bilgan holda foydalanish kerak
sayt korsatadigan ma'lumot user-agentga bog'liq bo'lishi mumkin
https://deviceatlas.com/blog/list-of-user-agent-strings  - user agentlar royxati
avtomatizatsiyada va test qilishda user agentlarni list bilan qo'llash kerak boladi
user-agentlar bilan ishlash uchun pythonda fake-useragent kutubxonasi bor, shundan foydalanaylik
useragent.ie, useragent.opera, useragent.random - useragentlarni tanlash metodlari
'''


# options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
# options.add_argument(f'user-agent={random.choice(user_agent_list)}')
options.add_argument(f'user-agent={useragent.random}')

driver = selenium.webdriver.Chrome(
    service=service,
    options=options
    )


try:
    driver.get(url2)
    driver.get_screenshot_as_file('instagram.png')
    driver.save_screenshot('screenshot5.png')
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
