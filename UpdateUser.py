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

#Test case for user register with credential data
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
