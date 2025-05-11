import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from curl import *
from pages.home_page import HomePageScooter
from pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

# В conftest.py
@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def home_page(driver):
    return HomePageScooter(driver)