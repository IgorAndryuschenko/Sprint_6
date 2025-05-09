import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageLocators:


    @staticmethod
    def accordion_number(number):
        return By.ID, f'accordion__heading-{number}'

    @staticmethod
    def text_response(number):
        return By.XPATH, f"//div[@aria-labelledby='accordion__heading-{number}']/p"


    BUTTON_ORDER_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']") # кнопка Заказать в хедере
    BUTTON_ORDER_MIDDLE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") # кнопка Заказать в хедере

    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")