from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key, Controller
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

#Test case for user want to see preview item before sell
def test_AddProduct_001_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/section/div/a/span').click()
    time.sleep(3)
    driver.find_element(By.ID, 'product_name').send_keys('Porsche 911 GT3 RS')
    driver.find_element(By.ID, 'product_price').send_keys('9000000000')
    select = Select(driver.find_element(By.ID, 'product_category_id'))
    select.select_by_visible_text('Kendaraan')
    driver.find_element(By.ID, 'product_description').send_keys('Alasan jual : Salah warna')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[5]/div'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\2023-porsche-911-gt3-rs-teaser-image")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/label[1]').click()
    time.sleep(3)
    assert 'Porsche 911 GT3 RS' in driver.find_element(By.CSS_SELECTOR, 'body > section > section > div > div.col-4 > div.card.p-2.rounded-4.shadow.border-0 > div > h5').text

#Test case for user want to update preview item before sell
def test_AddProduct_002_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/section/div/a/span').click()
    time.sleep(3)
    driver.find_element(By.ID, 'product_name').send_keys('Porsche 911 GT3 RS')
    driver.find_element(By.ID, 'product_price').send_keys('9000000000')
    select = Select(driver.find_element(By.ID, 'product_category_id'))
    select.select_by_visible_text('Kendaraan')
    driver.find_element(By.ID, 'product_description').send_keys('Alasan jual : Salah warna')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[5]/div'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\2023-porsche-911-gt3-rs-teaser-image")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/label[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/section/div/div[2]/div[1]/div/a[1]').click()
    time.sleep(2)
    driver.find_element(By.ID, 'product_description').clear()
    driver.find_element(By.ID, 'product_description').send_keys('Alasan jual : Salah beli')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/label[1]').click()
    time.sleep(3)
    assert 'Salah beli' in driver.find_element(By.XPATH, '/html/body/section/section/div/div[1]/div[2]/div/p').text
    
#Test case for user want to publish item after see preview item
def test_AddProduct_003_Positive(driver):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'ms-auto').click()
    time.sleep(2)
    driver.find_element(By.ID, 'user_email').send_keys('testingselenium@testing.com')
    driver.find_element(By.ID, 'user_password').send_keys('testing' + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/section/div/a/span').click()
    time.sleep(3)
    driver.find_element(By.ID, 'product_name').send_keys('Porsche 911 GT3 RS')
    driver.find_element(By.ID, 'product_price').send_keys('9000000000')
    select = Select(driver.find_element(By.ID, 'product_category_id'))
    select.select_by_visible_text('Kendaraan')
    driver.find_element(By.ID, 'product_description').send_keys('Alasan jual : Salah warna')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[5]/div'). click()
    time.sleep(3)

    keyboard = Controller()
    keyboard.type("C:\\Users\\toddi\\Downloads\\2023-porsche-911-gt3-rs-teaser-image")
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/section/section/div/form/div[6]/label[1]').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'commit').click()
    try:
        WebDriverWait(driver, 2).until(
            EC.invisibility_of_element_located((By.XPATH, "/html/body/section/section/div/div[2]/div[1]/div/form/input[5]"))
        )
        time.sleep(2)
        assert True  # If the notification is found, the test case is successful.
    except:
        assert False  # If the notification is found, the test case is fail.