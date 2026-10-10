# Pre-entrega QA Automation

Pruebas automatizadas sobre [Sauce Demo](https://www.saucedemo.com/) con Python, Selenium y pytest.

## Casos de prueba

- *test_login.py*: login exitoso con usuario válido.
- *test_inventory.py*: valida el título de la página, la presencia de productos, nombre y precio del primer producto, y que el menú y el filtro estén visibles.
- *test_cart.py*: agrega el primer producto, verifica que el contador del carrito suba a 1 y que el producto aparezca en el carrito.

## Cómo ejecutarlas


pip install pytest selenium pytest-html
pytest -v--html=reports/report.html

## Screenshots
-* reports/screenshort/  guarda automaticamentes las capturas de fallos y 
report_ejemplo_fallo_html muestra el ejemplo-


El reporte HTML se genera en reports/report.html.

## Tecnologías

Python, Selenium WebDriver, pytest, pytest-html


Autora: Anita Anheluk
