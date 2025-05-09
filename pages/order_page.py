from locators.locators_home_page import *
from locators.locators_order_page import *
from pages.base_page import *
from selenium.webdriver.common.keys import Keys
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage(BasePage):
    @allure.step("Кликнуть на кнопку Заказать в хедере")
    def click_bottom_order_header(self):
        self.click_on_element(HomePageLocators.BUTTON_ORDER_HEADER)

    @allure.step("Скролл до кнопки Заказать в середине страницы")
    def scroll_to_bottom_order_middle(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_MIDDLE)

    @allure.step("Кликнуть на кнопку Заказать в середине страницы")
    def click_bottom_order_middle(self):
        self.click_on_element(HomePageLocators.BUTTON_ORDER_MIDDLE)

    @allure.step("Ввести текст в поле Имя")
    def input_name(self, name):
        self.send_keys_to_input(OrderPageLocators.INPUT_NAME, name)

    @allure.step("Ввести текст в поле Фамилия")
    def input_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step("Ввести текст в поле Адрес")
    def input_address(self, address):
        self.send_keys_to_input(OrderPageLocators.INPUT_ADDRESS,address)

    @allure.step("Ввести текст и выбрать станцию в поле Метро")
    def input_metro(self, metro):
        self.send_keys_to_input(OrderPageLocators.INPUT_METRO_STATION, metro)
        element = self.wait_for_element(OrderPageLocators.INPUT_METRO_STATION)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Ввести текст в поле Телефон")
    def input_phone(self, phone):
        self.send_keys_to_input(OrderPageLocators.INPUT_PHONE_NUMBER,phone)


    @allure.step("Заполнить данные")
    def fill_data(self,name, surname, address, metro, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_metro(metro)
        self.input_phone(phone)

    @allure.step("Кликнуть на кнопку Далее после ввода данных")
    def click_button_further(self):
        self.click_on_element(OrderPageLocators.BUTTON_FURTHER)

    @allure.step("Ввести текст в поле Дата")
    def input_date(self, date):
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.send_keys_to_input(OrderPageLocators.INPUT_DATE, date)
        element=self.wait_for_element(OrderPageLocators.INPUT_DATE)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок заказа для первого тестового случая")
    def input_orger_period_1(self):
        self.click_on_element(OrderPageLocators.INPUT_ORDER_PERIOD)
        self.click_on_element(OrderPageLocators.INPUT_ORDER_PERIOD_1)

    @allure.step("Выбрать срок заказа для второго тестового случая")
    def input_orger_period_2(self):
        self.click_on_element(OrderPageLocators.INPUT_ORDER_PERIOD)
        self.click_on_element(OrderPageLocators.INPUT_ORDER_PERIOD_2)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Получить баннер подтверждения заказа")
    def is_order_confirmed(self):
        return self.wait_for_element(OrderPageLocators.CONFIRM_ORDER).is_displayed()

    @allure.step("Кликнуть на кнопку Да в подтверждении заказа")
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Получить баннер Заказ оформлен")
    def order_has_been_placed(self):
        return self.wait_for_element(OrderPageLocators.ORDER_HAS_BEEN_PLACED).is_displayed()

    @allure.step("Кликнуть на кнопку Посмотреть статус")
    def click_button_status(self):
        self.click_on_element(OrderPageLocators.BUTTON_STATUS)

