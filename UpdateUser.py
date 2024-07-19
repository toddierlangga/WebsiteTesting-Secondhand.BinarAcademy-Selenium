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
def test_UpdateUser_001_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('websitetest@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#navbarSupportedContent > div > ul > li.nav-item.dropdown.fs-5.d-none.d-lg-block > ul > li:nth-child(1) > a > div > div').click()
    time.sleep(1)
