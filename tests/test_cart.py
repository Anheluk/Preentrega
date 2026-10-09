import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import login

def test_cart():
    driver = webdriver.Chrome()

    try:
        login(driver)

        # Agregar el primer producto
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        nombre_producto = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        productos[0].find_element(By.TAG_NAME, "button").click()

        # Verificar que el contador se incrementa
        contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador.text == "1"

        # Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "cart" in driver.current_url

        # Verificar el producto en el carrito
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 1
        nombre_en_carrito = items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre_en_carrito == nombre_producto

    finally:
        driver.quit()