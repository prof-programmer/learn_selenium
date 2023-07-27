import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = "https://www.instagram.com/"


# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\automate_smartup\\chromedriver.exe")

# drayeverga adresni korsatishda 1 ta teskari slesh ishlatmoqchi bolsa 'r' (экранирование) dan foydalanish kerak
# r"D:\GitHubRepos\automate_smartup\chromedriver.exe"

options = selenium.webdriver.ChromeOptions()
driver = selenium.webdriver.Chrome(service=service, options=options)


try:
    driver.get(url)
    driver.get_screenshot_as_file('instagram.png')
    driver.save_screenshot('screenshot2.png')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()