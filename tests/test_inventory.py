import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import login

def test_inventory():
    driver = webdriver.Chrome()

    try:
        login(driver)

# Validacion del titulo de la pagina
        assert driver.title == "Swag Labs"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        assert (nombre_producto) == "Sauce Labs Backpack"
        assert (precio_producto) == "$29.99"

        #Verificacion de Menu
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()
        
        #Verrificacion filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()


    finally:
     driver.quit()

