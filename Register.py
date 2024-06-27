from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
def test_Register_001_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Daftar di sini').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_name').send_keys('Testing Selenium')
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').is_displayed()
    time.sleep(2)

#Test case for checking if data will be redundant if email is the same
def test_Register_002_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Daftar di sini').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_name').send_keys('Testing Selenium')
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#new_user > div:nth-child(3) > div.form-text.text-danger').is_displayed()
    time.sleep(2)