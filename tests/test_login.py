import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import login

def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        
        usuario = driver.find_element(By.ID, "user-name")
        password= driver.find_element(By.ID, "password")
        boton_login= driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        assert "/inventory.html" in driver.current_url

#Validacion Texto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.is_displayed()
    

        assert logo.text == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert len(titulo.text) > 0
        
    finally:
        driver.quit()
        