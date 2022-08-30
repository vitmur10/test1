import random
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from const import Token


def password_generator():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for n in range(1):
        password = ''
        for i in range(8):
            password += random.choice(chars)
        return password


password = password_generator()
date_of_birth = {'day': random.randrange(1, 28),
                 'month': random.randrange(1, 12),
                 'year': random.randrange(1985, 2006)
                 }
nickname = input('Nickname:')
email = str(input('Email:'))
if '@' not in email:
    print('The email must contain the @ symbol!!!')
    email = str(input('Email:'))

print(nickname, password, email)
# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")


options.add_argument("--disable-blink-features=AutomationControlled")

#options.headless = True
driver = webdriver.Chrome(
    executable_path=r"C:\Users\vital\OneDrive\Робочий стіл\test1\Chromedriver\chromedriver.exe",
    options=options
)

solver = TwoCaptcha(Token)

config = {
            'server':           '2captcha.com',
            'apiKey':           '6d2047f498b2f9d6dd6d823a876411dd',
            'softId':            123,
            'callback':         'https://discord.com/register',
            'defaultTimeout':    5,
            'recaptchaTimeout':  5,
            'pollingInterval':   5,
        }

solver = TwoCaptcha(**config)

result = solver.hcaptcha(sitekey='f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34',
                         url='https://discord.com/register')

try:
    driver.get("https://discord.com/register")
    email_input = driver.find_element(By.NAME, 'email')
    email_input.clear()
    email_input.send_keys(email)
    username_input = driver.find_element(By.NAME, 'username')
    username_input.clear()
    username_input.send_keys(nickname)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(password)
    day = driver.find_element(By.ID, 'react-select-2-input')
    day.clear()
    day.send_keys(date_of_birth['day'])
    year = driver.find_element(By.ID, 'react-select-4-input')
    year.clear()
    year.send_keys(date_of_birth['year'])
    month = driver.find_element(By.ID, 'react-select-3-input')
    month.clear()
    month.send_keys(date_of_birth['month'])
    month.send_keys(Keys.ENTER)
    month.send_keys(Keys.ENTER)
    month.send_keys(Keys.ENTER)
    time.sleep(15)
    code = solver.get_result(result)
except Exception as ex:
    print(ex)

finally:
    print(result)

