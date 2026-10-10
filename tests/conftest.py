import os
from datetime import datetime
import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            nombre = f"{item.name}{datetime.now():%Y%m%d%H%M%S}.png"
            driver.save_screenshot(os.path.join("reports", "screenshots", nombre))