from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_login_success():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    assert "/inventory.html" in driver.current_url
