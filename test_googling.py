from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://google.co.id')
    yield driver
    driver.quit()

def test_googling(driver):
    driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys('Toddi Erlangga' + Keys.ENTER)
    # driver.find_element('name', 'q').send_keys('Toddi Erlangga' + Keys.ENTER)
    assert 'Toddi Erlangga' in driver.find_element(By.CSS_SELECTOR, 'h3').text
    # assert 'Toddi Erlangga' in driver.find_element('css selector', 'h3').text
    assert 'Toddi Erlangga' in driver.title