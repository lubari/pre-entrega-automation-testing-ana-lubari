import pytest
from utils.helpers import is_element_present
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
    username_input.send_keys("standard_user")

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")
    
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url, "No se redirigió al inventario"


def test_verificar_catalogo(driver):
    login(driver)
    assert driver.title == "Swag Labs", f"Título Inesperado: {driver.title}"
    
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(products) > 0, "No se encontraron productos"
    print(f"Se encontraron {len(products)} productos en el catálogo")

    assert is_element_present(driver, By.CLASS_NAME, "shopping_cart_link")
    assert is_element_present(driver, By.ID, "react-burger-menu-btn")
    assert is_element_present(driver, By.CLASS_NAME, "product_sort_container")

    first_name  = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    first_price = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    print(f"Primer producto: {first_name} - {first_price}")


def test_interaccion_con_producto(driver):
    login(driver)

    assert not is_element_present(driver, By.CLASS_NAME, "shopping_cart_badge"), "El carrito debería estar vacío inicialmente"

    first_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
    first_item_name = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    
    first_item.find_element(By.TAG_NAME, "button").click()

    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "1", f"El contador del carrito es {badge}, se esperaba 1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, f"Debería haber 1 producto en el carrito, pero hay {len(cart_items)}"

    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item_name == first_item_name, f"El producto en el carrito ({cart_item_name}) no coincide con el añadido ({first_item_name})"

    
