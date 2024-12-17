import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(2)