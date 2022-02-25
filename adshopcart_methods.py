import sys
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import adshopcart_locators as locators


driver = webdriver.Chrome('C:/Users/Sirisha/PycharmProjects/pythonProject/chromedriver.exe')


def setUp():
    print(f'Test Start at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url and driver.title == driver.title:
        print(f'Welcome to Advantage online shopping homepage {driver.current_url} with Title {driver.title}')
    else:
        print(f'We are not at the Advantage online shopping homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Ended at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()


