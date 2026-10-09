from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(5)


try:
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    first_item = driver.find_element(By.CSS_SELECTOR, "div.inventory_item")
    first_item_name = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    first_item.find_element(By.TAG_NAME, "button").click() #añadir al carrito

    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "1", f"El contador del carrito es {badge} (se esperaba 1)"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_name = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
    assert cart_name == first_item_name, "El producto del carrito no coincide"
    print("Test OK")

    
finally:
    driver.quit()
    