from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key, Controller
import pytest
import time

#Webdriver controller
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://secondhand.binaracademy.org/')
    yield driver
    driver.quit()

#Test case for user update account with credential data
def test_UpdateUser_001_Positive(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)

    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')

    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_visible_text('Bandung')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('+628')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    assert 'Selenium' in driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div > div.fs-5.fw-bold').text

#Test case for user update account without fill the form
def test_UpdateUser_002_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    user_name = driver.find_element(By.ID, 'user_name').clear()
    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_visible_text('Bandung')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    if user_name is not None:
        if(user_name.get_attribute('required')):
            time.sleep(3)

#Test case for user update account with wrong pnohe number format
#This function will work because this is the bug
def test_UpdateUser_003_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)

    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')

    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_visible_text('Bandung')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('ABC')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div > div.fs-5.fw-bold'). click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    element = driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[5]/input')
    assert element.get_attribute('value') == 'ABC'

#Test case for user update account without fill name
def test_UpdateUser_004_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    user_name = driver.find_element(By.ID, 'user_name').clear()
    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_visible_text('Bandung')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('+628')
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    if user_name is not None:
        if(user_name.get_attribute('required')):
            time.sleep(3)

#Test case for user update account without fill city
def test_UpdateUser_005_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')
    select = Select(driver.find_element(By.ID, 'user_city_id'))
    city = select.select_by_index(0)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('+628')
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    if city is not None:
        if(city.get_attribute('required')):
            time.sleep(3)

#Test case for user update account without fill address
def test_UpdateUser_006_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')
    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_index(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    address = driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('+628')
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    if address is not None:
        if(address.get_attribute('required')):
            time.sleep(3)

#Test case for user update account without fill phone number
def test_UpdateUser_007_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Ecommerce-icon-Graphics-4123404-1")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')
    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_index(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    phone_number = driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    if phone_number is not None:
        if(phone_number.get_attribute('required')):
            time.sleep(3)

#Test case for user update account with wrong image format
#NOTE!!! once you execute this function, the account will be lock
def test_UpdateUser_008_Negative(driver):
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
    driver.find_element(By.ID, 'form-avatar-image'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\Doc31.pdf")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)

    driver.find_element(By.ID, 'user_name').clear()
    driver.find_element(By.ID, 'user_name').send_keys('Selenium')

    select = Select(driver.find_element(By.ID, 'user_city_id'))
    select.select_by_visible_text('Bandung')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.ID, 'user_address').clear()
    driver.find_element(By.ID, 'user_address').send_keys('Jalan-Jalan')
    driver.find_element(By.ID, 'user_phone_number').clear()
    driver.find_element(By.ID, 'user_phone_number').send_keys('+628')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/input').click()
    time.sleep(2)
    assert "We're sorry, but something went wrong." in driver.find_element(By.CSS_SELECTOR, 'h1').text