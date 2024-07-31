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
    
#Test case for user login with credential account
def test_Login_001_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[6]/a/i').is_displayed()
    time.sleep(3)

#Test case for login without fill form
def test_Login_002_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    email = driver.find_element(By.ID, 'user_email')
    email.clear()
    password = driver.find_element(By.ID, 'user_password')
    password.clear()
    driver.find_element(By.NAME, 'commit').click()
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user_email'='Please fill out this field.']"))
        )
        time.sleep(2)
        assert True  # If the notification is found, the test case is successful.
    except:
        assert False  # If the notification is found, the test case is fail.

#Test case for login without fill password
def test_Login_003_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    password = driver.find_element(By.ID, 'user_password')
    password.clear()
    driver.find_element(By.NAME, 'commit').click()

    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user_password'='Please fill out this field.']"))
        )
        time.sleep(2)
        assert True  # If the notification is found, the test case is successful.
    except:
        assert False  # If the notification is found, the test case is fail.

#Test case for login without fill email
def test_Login_004_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    email = driver.find_element(By.ID, 'user_email')
    email.clear()
    driver.find_element(By.ID, 'user_password').send_keys('testing')
    driver.find_element(By.NAME, 'commit').click()

    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user_email'='Please fill out this field.']"))
        )
        time.sleep(2)
        assert True  # If the notification is found, the test case is successful.
    except:
        assert False  # If the notification is found, the test case is fail.

#Test case for login within fill wrong email
def test_Login_005_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('websitetest_@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing')
    driver.find_element(By.NAME, 'commit').click()
    assert WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div')))

#Test case for login within fill wrong password
def test_Login_006_Negative(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing_')
    driver.find_element(By.NAME, 'commit').click()
    assert WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div')))