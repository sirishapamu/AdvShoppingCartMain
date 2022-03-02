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
    if driver.current_url == locators.adshopcart_url and driver.title == "\xa0Advantage Shopping":
        # driver.title == " Advantage Shopping"(copied from print driver.title)
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


def sign_up():
    assert driver.current_url == locators.adshopcart_url
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.5)
    if driver.current_url == locators.adshopcart_create_account_url:
        assert driver.find_element(By.XPATH, '//h3[contains(., "CREATE ACCOUNT")]').is_displayed()
        # Account details:
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
        sleep(0.25)
        # Personal Details:
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
        sleep(0.25)
        # Address:
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(0.25)
        # Checkbox and Register:
        checkbox = driver.find_element(By.NAME, 'i_agree')
        if checkbox.get_attribute('checked'):
            print('Checkbox is selected')
        else:
            driver.find_element(By.NAME, 'i_agree').click()
            print('checkbox not selected')
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.25)
        print(f'New user with Username - {locators.new_username} and Password - {locators.new_password} is created')
        sleep(0.5)


def check_account_info():
        # Checking Account information:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(0.5)
        # driver.find_element(By.XPATH, f'//span[contains(., "{locators.new_username}")]').click()
        driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[3]/a/div/label[1]').click()
        sleep(0.5)
        if driver.current_url == locators.adshopcart_myaccount_url:
            assert driver.find_element(By.XPATH, '//h3[contains(., "MY ACCOUNT")]').is_displayed()
            sleep(2)
            if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]'):
                print(f'Account details displays full name {locators.full_name}')
            else:
                print(f'This is not the user created')
        else:
            print(f'This is not My Account page')
        # Checking Orders Information:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[3]/a/div/label[2]').click()
        sleep(0.25)
        if driver.current_url == locators.adshopcart_myorders_url:
            assert driver.find_element(By.XPATH, '//h3[contains(., "MY ORDERS")]').is_displayed()
            sleep(2)
            if driver.find_element(By.XPATH, f'//label[contains(., " - No orders - ")]').is_displayed():
                print('Expected result "No Orders" is displayed')
            else:
                print('Expected result is not displayed')
        else:
            print('This is not My Orders page')


def logout():
        # Signout from account:
        driver.find_element(By.ID, 'menuUser').click()
        driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[3]/a/div/label[3]').click()
        print(f'User with username {locators.new_username} logged out')
        sleep(2)


def login(username, password):
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(5)
        print('before')
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)
        print(f'Login with Username - {locators.new_username}, Password - {locators.new_password}')


def delete_account():
    # Delete new created account:
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[3]/a/div/label[1]').click()
    sleep(0.5)
    if driver.current_url == locators.adshopcart_myaccount_url:
        assert driver.find_element(By.XPATH, '//h3[contains(., "MY ACCOUNT")]').is_displayed()
        sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[1]/div[6]/button/div').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/div[3]/div[1]').click()
        sleep(0.5)
        print('User account deleted successfully')
        sleep(5)
    else:
        print('Test failed')
        sleep(0.5)


def check_deleted_credentials():
    driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]').is_displayed()
    print('Expected message is displayed')











# setUp()
# sign_up()
# check_account_info()
# logout()
# login(locators.new_username, locators.new_password)
# delete_account()
# login(locators.new_username, locators.new_password)
# check_deleted_credentials()
# tearDown()


