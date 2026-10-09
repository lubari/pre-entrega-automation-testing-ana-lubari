import pytest
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import *



@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.maximize_window()

    yield driver

    driver.quit()

def test_login_success(driver):
    driver.get("https://www.saucedemo.com")
    driver.implicitly_wait(5)

    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    username_input.send_keys("standar_user")

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")
    
    driver.find_elements(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"


def test_verificar_catalogo(driver):
    login(driver)
