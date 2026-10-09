from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Al usar Selenium 4 y tener Firefox nativo, ¡esto es todo lo que necesitas!
driver = webdriver.Firefox()
driver.implicitly_wait(5)

try:
    driver.get('https://www.saucedemo.com')
    

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
   
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    assert driver.title == "Swag Labs", "Tiítulo Inesperado"

    print("Test OK")
    
finally:
    driver.quit()
