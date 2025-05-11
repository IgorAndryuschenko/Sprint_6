import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class OrderPageLocators:

    BUTTON_FURTHER = (By.XPATH,
                      "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    BUTTON_ORDER = (By.XPATH,
                      "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    BUTTON_YES = (By.XPATH,
                      "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

    BUTTON_STATUS = (By.XPATH,
                      "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    INPUT_NAME = (By.XPATH, "//input[@placeholder= '* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder= '* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder= '* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, "//input[@placeholder= '* Станция метро']")
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder= '* Телефон: на него позвонит курьер']")
    INPUT_DATE = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    INPUT_ORDER_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()= '* Срок аренды']")
    INPUT_ORDER_PERIOD_1= (By.XPATH, "//div[@role='option' and text()='сутки']")
    INPUT_ORDER_PERIOD_2= (By.XPATH, "//div[@role='option' and text()='двое суток']")


    CONFIRM_ORDER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()= 'Хотите оформить заказ?']")
    ORDER_HAS_BEEN_PLACED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()= 'Заказ оформлен']")


