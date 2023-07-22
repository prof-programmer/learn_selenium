import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = "https://www.instagram.com/"
url2 = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\automate_smartup\\chromedriver.exe")

# drayeverga adresni korsatishda 1 ta teskari slesh ishlatmoqchi bolsa 'r' (экранирование) dan foydalanish kerak
# r"D:\GitHubRepos\automate_smartup\chromedriver.exe"

# options
options = selenium.webdriver.ChromeOptions()

# user agent qoyamiz, istalgan user agent qoysa boladi, xohlasak android user agentni kiritsak boladi
# options.add_argument('user-agent=HelloWorld')
options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
driver = selenium.webdriver.Chrome(
    service=service,
    options=options
    )


try:
    driver.get(url2)
    driver.get_screenshot_as_file('instagram.png')
    driver.save_screenshot()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
